from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView




class SignUpView(CreateView):
    from_class= UserCreationForm
    sucess_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
