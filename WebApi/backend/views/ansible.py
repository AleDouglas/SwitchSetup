from datetime import datetime
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView
from backend.DAL.DAO.logDAO import *
from backend.DAL.DAO.deviceDAO import *
from backend.integrations.ansible import *
from backend.DAL.models.ansible import *
from django.urls import reverse_lazy
from django.core.exceptions import ValidationError
from backend.views.utils import AdminRequired


class AnsibleView(LoginRequiredMixin, TemplateView):
    template_name = 'ansible.html'



class AnsibleDefaultView(LoginRequiredMixin, TemplateView):
    template_name = 'ansibleDefault.html'
    ansible = AnsibleSwitchConnector()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        credentials = getAllDeviceCredential()
        context['credentials'] = credentials
        return context

    def execute_command(self, playbook, host, switch, username, password, ansible_level):
        # Adicionar verificações de segurança aqui
        try:
            self.ansible.write_ansible_playbook(playbook, str(switch))
            self.ansible.write_ansible_host(host, switch = str(switch), username = username, password = password)
            output = self.ansible.run_ansible(ansible_level)
            return output
        except:
            return "Error when trying to run ansible"

    def post(self, request ,*args, **kwargs):
        playbook = request.POST.get('playbook')
        ansible_level = request.POST.get('ansible_level')
        host = request.POST.get('host')
        switch = request.POST.get('switch')
        username = request.POST.get('username')
        password = request.POST.get('password')
        if request.POST.get('credential') == "none":
            output = self.execute_command(playbook, host, switch, username, password, ansible_level)
        else:
            credential = getDeviceCredential(request.POST.get('credential'))
            output = self.execute_command(playbook, host, switch, credential.username, credential.password, ansible_level)
        createLog(
            user=f"{request.user}",
            date=datetime.now().strftime("%d-%m-%Y"),
            hour=datetime.now().strftime("%H:%M:%S"),
            switch=switch,
            playbook=playbook,
            host=host,
            output=output,
        )
        return self.render_to_response(self.get_context_data(output = output))


class PlaybookCustomView(AdminRequired, CreateView):
    template_name = 'ansibleForms.html'
    model = PlaybookCustom
    fields = ['title', 'about', 'playbook_file']
    success_url = reverse_lazy("playbookCustom")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = '1'
        return context

    def form_valid(self, form):
        playbook_file = form.cleaned_data['playbook_file'] 

        if not playbook_file.name.endswith('.yml'):
            context = self.get_context_data(form=form, result="Error: Only .py files are allowed.")
            return self.render_to_response(context)
    
        form.save()
        context = self.get_context_data(form=form, result="Successful uploading files")
        return self.render_to_response(context)

    def form_invalid(self, form):
        context = self.get_context_data(form=form, result="Failed to upload files")
        return self.render_to_response(context)


class HostCustomView(AdminRequired, CreateView):
    template_name = 'ansibleForms.html'
    model = HostCustom
    fields = ['title', 'about', 'host_file']
    success_url = reverse_lazy("hostCustom")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = '2'
        return context

    def form_valid(self, form):
        host_file = form.cleaned_data['host_file'] 

        if not host_file.name.endswith('.yml'):
            context = self.get_context_data(form=form, result="Error: Only .py files are allowed.")
            return self.render_to_response(context)
    
        form.save()
        context = self.get_context_data(form=form, result="Successful uploading files")
        return self.render_to_response(context)

    def form_invalid(self, form):
        context = self.get_context_data(form=form, result="Failed to upload files")
        return self.render_to_response(context)


class AnsibleCustomView(LoginRequiredMixin, TemplateView):
    template_name = 'ansibleCustom.html'
    ansible = AnsibleSwitchConnector()


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        playbook = PlaybookCustom.objects.all()
        host = HostCustom.objects.all()
        context['playbook_list'] = playbook
        context['host_list'] = host
        return context

    def execute_command(self, path_playbook, path_host, ansible_level):
        # Adicionar verificações de segurança aqui
        try:
            output = self.ansible.run_ansible_custom(path_playbook, path_host, ansible_level)
            return output
        except:
            return "Error when trying to run ansible"

    def post(self, request ,*args, **kwargs):
        playbook_file = request.POST.get('playbook_file')
        host_file = request.POST.get('host_file')

        path_playbook = PlaybookCustom.objects.get(id=int(playbook_file))
        path_host = HostCustom.objects.get(id=int(host_file))

        output = f"Playbook: {path_playbook.playbook_file.url}"

        return self.render_to_response(self.get_context_data(output = output))

