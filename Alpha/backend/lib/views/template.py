# Django import
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponse, HttpResponseForbidden
from datetime import datetime
# Database
from backend.lib.database.project import Project

# Methods
from backend.lib.methods.project import GetProject
from backend.lib.ansible.ansible import Ansible

# Terceiros
class TaskTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'pages/project/project_template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project_id = self.kwargs.get('project_id')
        try:
            if self.request.user.is_staff == True:
                project_data = GetProject.only(id=project_id)
            else:
                project_data = GetProject.member(id=project_id, user=self.request.user)
            context['project_data'] = project_data
            context['project_id'] = project_data.id
            context['project_title'] = project_data.title
            context['project_password'] = project_data.password
            context['project_owner'] = project_data.owner
            context['project_members'] = project_data.members
            context['project_playbooks'] = project_data.playbooks
            context['project_inventories'] = project_data.inventories
            context['project_templates'] = project_data.templates

        except Exception as e:
            print(f"Acesso negado: {e}")
        return context

    def render_to_response(self, context, **response_kwargs):
        if context['project_data'] == False:
            return redirect('home')
        return super().render_to_response(context, **response_kwargs)





@csrf_exempt
@require_POST
@login_required
def create_template(request):
    project_id = request.POST.get('project_id', '')
    title = request.POST.get('title', '')
    version = request.POST.get('version', '')
    playbook = request.POST.get('playbook', '')
    inventory = request.POST.get('inventory', '')

    if project_id:
        try:
            # Verifica se o usuário é o proprietário do projeto
            project = GetProject.owner(id=project_id, owner=request.user)
            # Pegando Playbook e Inventário
            get_playbook = GetProject.only_playbook(project=project, owner=request.user, playbook_id=playbook)
            get_inventory = GetProject.only_inventory(project=project, owner=request.user, inventory_id=inventory)

            template = GetProject.create_template(author=request.user,project = project, title=title, version=version, playbook=get_playbook, inventory= get_inventory)
            activity = GetProject.create_activity(project = project, user=request.user, description=f'User #{request.user.id} added a new template ID #{template.id}')
            # Activity register
            return JsonResponse(
                    {
                        'success': True,
                        'template_author_first_name': template.author.first_name,
                        'template_author_last_name': template.author.last_name,
                        'template_id': template.id, 
                        'template_title': template.title,
                        'template_version': template.version,
                        'template_playbook': template.playbook.title,
                        'template_inventory': template.inventory.title,
                    }
                )
            
        except:
            return JsonResponse({'success': False, 'result': 'Template not found'})


@csrf_exempt
@require_POST
@login_required
def delete_template(request, project_id, template_id):
    try:
        project = GetProject.owner(id=project_id, owner=request.user)
        template = project.templates.get(id=int(template_id))
        if template == False:
            return JsonResponse({'success': False, 'result': 'Template not found'})
        # REGISTER ACTIVITY
        activity = GetProject.create_activity(project = project, user=request.user, description=f'USER #{request.user.id} delete template #{template.id}')
        project.templates.remove(template)
        return JsonResponse({'success': True, 'result': 'Template delete successfully'})
    except Template.DoesNotExist:
        return JsonResponse({'success': False, 'result': 'Template not found'})


@csrf_exempt
@require_POST
@login_required
def execute_template(request, project_id, template_id):
    try:
        if request.user.is_staff:
            project = GetProject.only(id=project_id)
        else:
            project = GetProject.member(id=project_id, user=request.user)
        template = GetProject.only_template(project=project, owner=request.user, template_id=template_id)
        if template == False:
            return JsonResponse({'success': False, 'result': 'Template not found'})

        path_playbook = template.playbook.playbook_file.url[1:]
        path_inventory = template.inventory.inventory_file.url[1:]
        ansible_task, stdout_complete, terminal_output, status  = Ansible.run_ansible(path_playbook = path_playbook, path_inventory=path_inventory)
        get_terminal_output = []
        task_output = ''
        for x in terminal_output:
            get_date_time = datetime.now()
            time = f'[{get_date_time.strftime("%I:%M:%S %p")}]'
            get_output = f'<div class="div_output"><span class="hour_output">{time}</span><span style="margin-left: 15px;"><pre>{x}</pre></span></div>'
            get_terminal_output.append(get_output)
            task_output += f'{get_output}'

        # GENERATE A NEW TASK
        task = GetProject.create_task(title=f'USER #{request.user.id} run a template ID #{template_id}', author=request.user, status=status, output=task_output, template_id=template_id)
        # ACTIVITY REGISTER
        activity = GetProject.create_activity(project = project, user=request.user, description=f'USER #{request.user.id} run a template ID #{template_id}')

        return JsonResponse({'success': True, 'status': status,'result': 'Template was execute successfully', 'ansible':ansible_task, 'terminal_output':get_terminal_output, 'task_id': task.id, 'template_title':template.title })
    except Exception as e:
        print(e)
        return JsonResponse({'success': False, 'result': 'Template not found', 'status': 0})



