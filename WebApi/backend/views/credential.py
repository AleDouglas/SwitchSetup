from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView, DeleteView
from backend.DAL.DAO.deviceDAO import *
from backend.views.utils import AdminRequired
from backend.DAL.models.device import DeviceCredential
from django.urls import reverse_lazy
from datetime import datetime
from backend.DAL.DAO.logDAO import *


class CredentialPageView(AdminRequired, TemplateView):
    template_name = 'credential.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['credentials'] = getAllDeviceCredential()
        context['settings'] = 0
        context['page'] = "Credentials"
        return context

    def post(self, request ,*args, **kwargs):
        createCredential(
            title = request.POST.get('title'),
            username = request.POST.get('username'),
            password = request.POST.get('password'),
        )
        result = "The credentials have been successfully upgraded."
        createLog(
            user=f"{request.user}",
            service=f"New credentials were saved in the system",
            description=f"Credentials can be used to execute Ansible without the need to enter a username and password",
            data=datetime.now().strftime("%d/%m/%Y"),
            hour=datetime.now().strftime("%H:%M:%S"),
            playbook="Unused function",
            host="Unused function",
            output=result,
        )
        return self.render_to_response(self.get_context_data(result = result))


class UpdateCredentialView(AdminRequired, UpdateView):
    template_name = 'credential.html'
    model = DeviceCredential
    fields = ['title','username','password']
    success_url = reverse_lazy("credentialList")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['settings'] = 1
        context['page'] = "Manage Credentials"
        return context


class DeleteCredentialView(AdminRequired, DeleteView):
    template_name = 'credential.html'
    model = DeviceCredential
    success_url = reverse_lazy("credentialList")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['settings'] = 2
        context['page'] = "Delete Credentials"
        return context
