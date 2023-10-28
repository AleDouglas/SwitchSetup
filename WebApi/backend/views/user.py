from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, UpdateView, DeleteView
from backend.DAL.models.user import CustomUser
from backend.forms import CustomUserCreationForm, CustomUserChangeForm
from django.urls import reverse_lazy
from django.db.models import Q
from backend.views.utils import AdminRequired
from backend.DAL.DAO.logDAO import *
from datetime import datetime


class UserPageView(AdminRequired, TemplateView):
    template_name = 'tableUser.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CustomUserCreationForm()
        users = CustomUser.objects.all()
        context['users'] = users
        return context

    def post(self, request ,*args, **kwargs):
        form = CustomUserCreationForm(request.POST)
        context = self.get_context_data()
        if form.is_valid():
            user = form.save()
            result = "Success in creating user"
            createLog(
            user=f"{request.user}",
            service=f"A new user has been added to the system",
            description=f"A new user has been added to the system",
            data=datetime.now().strftime("%d/%m/%Y"),
            hour=datetime.now().strftime("%H:%M:%S"),
            playbook="Unused function",
            host="Unused function",
            output="A new user has been created",
            )
            context['result'] = result
            return render(request, self.template_name, context)
        else:
            result = "Error in creating user"
            createLog(
            user=f"{request.user}",
            service=f"Attempt to add a new user",
            description=f"Attempt to add a new user",
            data=datetime.now().strftime("%d/%m/%Y"),
            hour=datetime.now().strftime("%H:%M:%S"),
            playbook="Unused function",
            host="Unused function",
            output="Attempted to generate a new user, but an error occurred.",
            )
            context['result'] = result
            return render(request, self.template_name, context)


class UpdateUserView(AdminRequired, UpdateView):
    template_name = 'updateUser.html'
    model = CustomUser
    fields = ['first_name','last_name','username','email','is_staff']
    success_url = reverse_lazy("userList")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['settings'] = 0
        context['page'] = "Edit User Information"
        return context


class DeleteUserView(AdminRequired, DeleteView):
    template_name = 'updateUser.html'
    model = CustomUser
    success_url = reverse_lazy("userList")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['settings'] = 1
        context['page'] = "Delete User"
        return context