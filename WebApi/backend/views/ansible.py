from datetime import datetime
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from backend.DAL.DAO.logDAO import *
from backend.integrations.ansible import *

class AnsibleView(LoginRequiredMixin, TemplateView):
    template_name = 'ansible.html'
    ansible = AnsibleSwitchConnector()

    def execute_command(self, playbook, host, switch, username, password):
        # Adicionar verificações de segurança aqui
        try:
            self.ansible.write_ansible_playbook(playbook, str(switch))
            self.ansible.write_ansible_host(host, str(switch), username, password)
            output = self.ansible.run_ansible()
            return output
        except:
            return "Error when trying to run ansible"

    def post(self, request ,*args, **kwargs):
        playbook = request.POST.get('playbook')
        host = request.POST.get('host')
        switch = request.POST.get('switch')
        username = request.POST.get('username')
        password = request.POST.get('password')
        output = self.execute_command(playbook, host, switch, username, password)
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