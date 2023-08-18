from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from backend.views.utils import AdminRequired
from backend.DAL.DAO.apiDAO import *
from backend.DAL.DAO.logDAO import *
from backend.DAL.models.api import ApiKey
from backend.integrations.ansible import *
from datetime import datetime



class ApiPageView(AdminRequired, TemplateView):
    template_name = 'api.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['settings'] = 0
        context['keys'] = getAllApi()
        context['page'] = "Manage Keys"
        return context

    def post(self, request ,*args, **kwargs):
        createKey(
            title = request.POST.get('title'),
        )
        result = "The key have been successfully upgraded."
        createLog(
            user=f"{request.user}",
            date=datetime.now().strftime("%d-%m-%Y"),
            hour=datetime.now().strftime("%H:%M:%S"),
            switch="Unused function",
            playbook="Unused function",
            host="Unused function",
            output="The user generated an API access key.",
        )
        return self.render_to_response(self.get_context_data(result = result))

class ApiDeleteView(AdminRequired, DeleteView):
    template_name = 'api.html'
    model = ApiKey
    success_url = reverse_lazy("apiKey")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['settings'] = 1
        context['page'] = "Delete Key"
        return context


class ApiResponseView(APIView):

    def execute_command(self, playbook, host, switch, username, password):
        # Adicionar verificações de segurança aqui
        try:
            self.ansible.write_ansible_playbook(string = playbook, switch = str(switch))
            self.ansible.write_ansible_host(string = host, switch = str(switch), username = username, password = password)
            output = self.ansible.run_ansible()
            return output
        except:
            return "Error when trying to run ansible"

    def post(self, request, format=None):
        data = request.data
        key = searchApi(data['key'])
        if key == False:
            return Response("Key not found, access denied")
        try:
            output = execute_command(playbook = data['command'], host = data['host'], switch = data['switch'], username = data['username'], password = data['password'])
            return Response(output)
        except:
            return Response("Please verify the variables used, remembering that the following fields are required: key, command, host, switch, username, password.")
