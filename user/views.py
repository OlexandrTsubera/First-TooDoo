from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, TemplateView, FormView
from user.forms import *

from user.models import *


class UserRegistrationView(CreateView):
    form_class = UserRegister
    template_name = 'user/register.html'
    success_url = reverse_lazy('home')


class Login(FormView):
    template_name = 'user/login.html'
    form_class = Login
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            form.add_error(None, 'Invalid username or password')
            return self.form_invalid(form)


class Logout(LogoutView):
    template_name = 'user/logout.html'
    success_url_allowed_hosts = reverse_lazy('home')


def confirm(request):
    return render(request, 'user/confirm_logout.html')


class Profile(LoginRequiredMixin, TemplateView):
    template_name = 'user/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
