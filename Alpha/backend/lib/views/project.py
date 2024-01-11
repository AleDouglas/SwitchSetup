# Django import
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Database
from backend.lib.database.project import Project

# Methods
from backend.lib.methods.project import GetProject

class ProjectView(LoginRequiredMixin, TemplateView):
    template_name = 'pages/project/project_project.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project_list'] = GetProject.filter_member(self.request.user)
        return context

@csrf_exempt
@require_POST
@login_required
def create_project(request):
    title = request.POST.get('title', '')
    password = request.POST.get('password', '')
    project = GetProject.create(title=title, password=password, owner=request.user)
    project.members.add(request.user)
    # ACTIVITY REGISTER
    activity = GetProject.create_activity(project = project, user=request.user, description=f'USER #{request.user.id} created a new project #{project.id}')
    return JsonResponse({'success': True, 'project_id': project.id, 'project_title': project.title})

@csrf_exempt
@require_POST
@login_required
def delete_project(request, project_id):
    try:
        project = GetProject.owner(id=project_id, owner=request.user)
        activity = GetProject.create_activity(project = project, user=request.user, description=f'USER #{request.user.id} delete project #{project_id}')
        members = project.members.all()
        for x in members:
            project.members.remove(x)
        return JsonResponse({'success': True, 'message': 'Project deleted successfully.'})
    except Project.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Project not found or you do not have permission to delete it.'})
