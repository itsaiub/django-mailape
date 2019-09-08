from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView

from . import models, forms
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
