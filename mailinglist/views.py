from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DeleteView, DetailView
from django.core.exceptions import PermissionDenied

from . import models, forms, mixins
# Create your views here.


class MailingList(LoginRequiredMixin, ListView):
    template_name = 'mailinglist/mailinglist_list.html'

    def get_queryset(self):
        return models.MailingList.objects.filter(owner=self.request.user)


class CreateMailingList(LoginRequiredMixin, CreateView):
    form_class = forms.MailingListForm
    template_name = 'mailinglist/mailinglist_form.html'

    def get_initial(self):
        return {
            'owner': self.request.user.id,
        }


class DeleteMailingList(LoginRequiredMixin, mixins.UserCanUseMailingList, DeleteView):
    model = models.MailingList

    template_name = 'mailinglist/mailinglist_confirm_delete.html'

    success_url = reverse_lazy('mailinglist:mailinglist_list')


class DetailMailingList(LoginRequiredMixin, mixins.UserCanUseMailingList, DetailView):
    model = models.MailingList

    template_name = 'mailinglist/mailinglist_details.html'


class SubscribeToMailList(CreateView):
    form_class = forms.SubscriberForm
    template_name = 'mailinglist/subscriber_form.html'

    def get_initial(self):
        return {
            'mailing_list': self.kwargs['mailinglist_id']
        }

    def get_success_url(self):
        return reverse('mailinglist:subscriber_thankyou', kwargs={
            'pk': self.object.mailing_list.id,
        })

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        mailing_list_id = self.kwargs['mailinglist_id']
        ctx['mailing_list'] = get_object_or_404(
            models.MailingList,
            id=mailing_list_id,
        )
        return ctx


class ThanksForSubs(DetailView):
    model = models.MailingList
    template_name = 'mailinglist/subscription_thanks.html'


class ConfirmSubscriptionView(DetailView):
    model = models.Subscriber
    template_name = 'mailinglist/confirm_subscription.html'

    def get_object(self, queryset=None):
        subscriber = super().get_object(queryset=queryset)
        subscriber.confirmed = True
        subscriber.save()
        return subscriber


class UnsubscribeView(DeleteView):
    model = models.Subscriber
    template_name = 'mailinglist/unsubscribe.html'

    def get_success_url(self):
        mailing_list = self.object.mailing_list
        return reverse(
            'mailinglist:subscribe',
            kwargs={
                'mailinglist_pk': mailing_list.id
            }
        )


class CreateMessage(LoginRequiredMixin, CreateView):
    SAVE_ACTION = 'save'
    PREVIEW_ACTION = 'preview'

    form_class = forms.MessageForm

    template_name = 'mailinglist/message_form.html'

    def get_success_url(self):
        return reverse(
            'mailinglist:manage_mailinglist',
            kwargs={
                'pk': self.object.mailing_list.id
            }
        )

    def get_initial(self):
        mailing_list = self.get_mailing_list()
        return {
            'mailing_list': mailing_list.id,
        }

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        mailing_list = self.get_mailing_list()
        ctx.update({
            'mailing_list': mailing_list,
            'SAVE_ACTION': self.SAVE_ACTION,
            'PREVIEW_ACTION': self.PREVIEW_ACTION
        })
        return ctx

    def form_valid(self, form):
        action = self.request.POST.get('action')
        if action == self.PREVIEW_ACTION:
            context = self.get_context_data(
                form=form,
                message=form.instance
            )
            return self.render_to_response(context=context)

        elif action == self.SAVE_ACTION:
            return super().form_valid(form)

    def get_mailing_list(self):
        mailing_list = get_object_or_404(
            models.MailingList, id=self.kwargs['mailinglist_pk'])

        if not mailing_list.user_can_use_mailing_list(self.request.user):
            raise PermissionDenied()
        return mailing_list


class MessageDetail(LoginRequiredMixin, mixins.UserCanUseMailingList, DetailView):
    model = models.Message
    template_name = 'mailinglist/message_detail.html'
