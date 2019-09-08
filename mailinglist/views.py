from django.urls import reverse_lazy
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
