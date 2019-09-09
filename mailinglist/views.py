from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DeleteView, DetailView

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
        print(self.kwargs['mailinglist_id'])
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
