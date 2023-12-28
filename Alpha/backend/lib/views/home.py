from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'pages/home.html'


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('home')