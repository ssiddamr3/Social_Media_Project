from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from . import forms

class Signup(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('test')
    template_name = 'accounts/signup.html'
