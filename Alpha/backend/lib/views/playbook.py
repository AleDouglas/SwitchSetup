# Django import
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime
# Database
from backend.lib.database.project import Project

# Methods
from backend.lib.methods.project import GetProject

class PlaybookView(LoginRequiredMixin, TemplateView):
    template_name = 'pages/project/project_playbook.html'

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
def create_playbook(request):
    project_id = request.POST.get('project_id', '')
    title = request.POST.get('title', '')
    description = request.POST.get('description', '')
    playbook_file = request.FILES.get('playbook_file', None)

    if project_id:
        try:
            project_data = GetProject.owner(id=project_id, owner=request.user)
            playbook = GetProject.create_playbook(title=title, description=description, playbook_file=playbook_file)
            project_data.playbooks.add(playbook)
            activity = GetProject.create_activity(project_id = project_id, user=request.user, description=f'USER #{request.user.id} added a new playbook #{playbook.id}')
            return JsonResponse(
                    {
                        'success': True, 
                        'playbook_id': playbook.id, 
                        'playbook_title': playbook.title,
                        'playbook_description': playbook.description,
                        'playbook_time': playbook.date_time,
                    }
                )
            
        except Project.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Playbook not found.'})


@csrf_exempt
@require_POST
@login_required
def delete_playbook(request, project_id, playbook_id):
    try:
        project = GetProject.owner(id=project_id, owner=request.user)
        playbook = project.playbooks.get(id=playbook_id)
        if playbook == False:
            return JsonResponse({'success': False, 'message': 'Playbook not found.'})
        activity = GetProject.create_activity(project_id = project_id, user=request.user, description=f'USER #{request.user.id} delete playbook #{playbook_id}')
        project.playbooks.remove(playbook)
        return JsonResponse({'success': True, 'message': 'Playbook deleted successfuly'})
    except Project.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Playbook not found.'})



