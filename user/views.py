from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

# Create your views here.


class RegisterView(CreateView):
    template_name = 'user/register.html'
    form_class = UserCreationForm
