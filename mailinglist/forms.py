from django import forms
from django.contrib.auth import get_user_model
from . import models


class SubscriberForm(forms.ModelForm):
    mailing_list = forms.ModelChoiceField(
        widget=forms.HiddenInput,
        queryset=models.MailingList.objects.all(),
        disabled=True
    )

    class Meta:
        model = models.Subscriber
        fields = ['mailing_list', 'email', ]


class MessageForm(forms.ModelForm):
    mailing_list = forms.ModelChoiceField(
        widget=forms.HiddenInput,
        queryset=models.MailingList.objects.all(),
        disabled=True
    )

    class Meta:
        model = models.Message
        fields = ['mailing_list', 'subject', 'body', ]


class MailingListForm(forms.ModelForm):
    owner = forms.ModelChoiceField(
        widget=forms.HiddenInput,
        queryset=get_user_model().objects.all(),
        disabled=True
    )

    class Meta:
        model = models.MailingList
        fields = ['owner', 'name', ]
