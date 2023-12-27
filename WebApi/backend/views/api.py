from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from backend.views.utils import AdminRequired
from backend.DAL.DAO.apiDAO import *
from backend.DAL.DAO.logDAO import *
from backend.DAL.DAO.ansibleDAO import *
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
            service=f"A new API access key was generated",
            description=f"Generated key provides access with permissions for additional API functions using POST methods.",
            data=datetime.now().strftime("%d/%m/%Y"),
            hour=datetime.now().strftime("%H:%M:%S"),
            playbook="Unused Service",
            host="Unused Service",
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
    ansible = AnsibleSwitchConnector()

    def execute_command(self, playbook, host, switch, username, password, ansible_level):
        # Adicionar verificações de segurança aqui
        try:
            self.ansible.write_ansible_playbook(string = playbook, switch = str(switch))
            self.ansible.write_ansible_host(string = host, switch = str(switch), username = username, password = password)
            output = self.ansible.run_ansible(ansible_level)
            return output
        except:
            return "Error when trying to run ansible"

    def post(self, request, format=None):
        data = request.data
        key = searchApi(data['key'])
        if key == False:
            return Response("Key not found, access denied")
        try:
            output = execute_command(playbook = data['command'], host = data['host'], switch = data['switch'], username = data['username'], password = data['password'], ansible_level = data['ansible_level'])
            
            createLog(
            user=f"Api Key",
            service=f"API-Based Service System",
            description=f"The user, represented by the key in the system, utilized access key services to execute Ansible with customizable playbook and host.",
            data=datetime.now().strftime("%d/%m/%Y"),
            hour=datetime.now().strftime("%H:%M:%S"),
            playbook=f"{data['command']}",
            host=f"{data['host']}",
            output=output,
            )
            return Response(output)
        except:
            return Response("Please verify the variables used, remembering that the following fields are required: key, command, host, switch, username, password.")


# Objetivo: Executar um playbook e um host já configurados no sistema
class ApiCustomResponseView(APIView):
    ansible = AnsibleSwitchConnector()

    def execute_command(self, path_playbook, path_host, ansible_level):
        output = self.ansible.run_ansible_custom(path_playbook=path_playbook, path_host=path_host, ansible_level=ansible_level)
        return output

    def post(self, request, format=None):
        data = request.data
        try:
            key = searchApi(data['key'])
        except Exception as e:
            return Response(f"Error: {str(e)}")
        if key == False:
            return Response("Key not found, access denied")
        try:            
            output = self.execute_command(path_playbook= str(data['playbook']), path_host= str(data['host']), ansible_level= data['ansible_level'])
            createLog(
            user=f"Api Key",
            service=f"API-Based Service System",
            description=f"The user, represented by the key in the system, utilized access key services to execute Ansible with predefined playbook and host settings.",
            data=datetime.now().strftime("%d/%m/%Y"),
            hour=datetime.now().strftime("%H:%M:%S"),
            playbook=f"{data['playbook']}",
            host=f"{data['host']}",
            output=output,
            )
            return Response(output)
        except Exception as e:
            return Response(f"Error: {str(e)}")


# Objetivo: Executar comandos customizáveis para um Host já configurado
class ApiHostDefault(APIView):
    ansible = AnsibleSwitchConnector()

    def execute_command(self, command, path_host, ansible_level, switch = "Cisco"):
        output = self.ansible.run_ansible_device(playbook_command=command, path_host=path_host, ansible_level=ansible_level, switch=switch)
        return output

    def post(self, request, format=None):
        data = request.data
        try:
            key = searchApi(data['key'])
        except Exception as e:
            return Response(f"Error: {str(e)}")
        if key == False:
            return Response("Key not found, access denied")
        try:            
            output = self.execute_command(command= str(data['command']), path_host= str(data['host']), ansible_level= data['ansible_level'])
            createLog(
            user=f"Api Key",
            service=f"API-Based Service System",
            description=f"The user, represented by the key in the system, utilized access key services to execute Ansible with a predefined host in the system, while the playbook was fully customizable.",
            data=datetime.now().strftime("%d/%m/%Y"),
            hour=datetime.now().strftime("%H:%M:%S"),
            playbook=f"{data['command']}",
            host=f"{data['host']}",
            output=output,
            )
            return Response(output)
        except Exception as e:
            return Response(f"Error: {str(e)}")



class ApiGetPlaybook(APIView):
    def post(self, request, format=None):
        data = request.data
        key = False
        try:
            key = searchApi(data['key'])
        except Exception as e:
            return Response(f"Error: {str(e)}")
        if key == False:
            return Response("Key not found, access denied")
        try:    
            jsonFormat = []     
            queryset = GetPlaybook.all()
            for playbook in queryset:
                tmp = {
                    "id": playbook.id,
                    "device": playbook.device,
                    "switch": playbook.switch,
                    "title": playbook.title,
                    "about": playbook.about,
                    "url": playbook.playbook_file.url
                }
                jsonFormat.append(tmp)
            return Response(jsonFormat)
        except Exception as e:
            return Response(f"Error: {str(e)}")

class ApiGetHost(APIView):
    def post(self, request, format=None):
        data = request.data
        key = False
        try:
            key = searchApi(data['key'])
        except Exception as e:
            return Response(f"Error: {str(e)}")
        if key == False:
            return Response("Key not found, access denied")
        try:            
            jsonFormat = []     
            queryset = getAllHost()
            for host in queryset:
                tmp = {
                    "id": host.id,
                    "device": host.device,
                    "switch": host.switch,
                    "title": host.title,
                    "about": host.about,
                    "url": host.host_file.url
                }
                jsonFormat.append(tmp)
            return Response(jsonFormat)
        except Exception as e:
            return Response(f"Error: {str(e)}")

class ApiGetCommandLine(APIView):
    def post(self, request, format=None):
        data = request.data
        key = False
        try:
            key = searchApi(data['key'])
        except Exception as e:
            return Response(f"Error: {str(e)}")
        if key == False:
            return Response("Key not found, access denied")
        try:    
            jsonFormat = []     
            queryset = getAllCommand()
            for command in queryset:
                tmp = {
                    "id": command.id,
                    "title": command.title,
                    "description": command.description,
                    "command": command.command,
                    "switch": command.switch,
                }
                jsonFormat.append(tmp)
            return Response(jsonFormat)
        except Exception as e:
            return Response(f"Error: {str(e)}")
    