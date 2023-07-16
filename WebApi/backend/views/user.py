from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, UpdateView, DeleteView
from backend.DAL.models.user import CustomUser
from backend.forms import CustomUserCreationForm, CustomUserChangeForm
from django.urls import reverse_lazy
from django.db.models import Q
from backend.views.utils import AdminRequired


class UserPageView(AdminRequired, TemplateView):
    template_name = 'tableUser.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        users = CustomUser.objects.all()
        context['users'] = users
        return context

    def post(self, request ,*args, **kwargs):
        username = request.POST['username']
        users = CustomUser.objects.filter(Q(username__icontains=username))
        return render(request, self.template_name, {'users': users})


class CreateUserView(AdminRequired, TemplateView):
    template_name = 'addUser.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CustomUserCreationForm()
        return context

    def post(self, request ,*args, **kwargs):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            result = "Success in creating user"
            return render(request, self.template_name, {'result': result})
        else:
            result = "Error in creating user"
            return render(request, self.template_name, {'result': result})


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