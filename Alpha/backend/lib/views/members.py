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
from backend.lib.database.user import CustomUser
# Methods
from backend.lib.methods.project import GetProject

class MembersView(LoginRequiredMixin, TemplateView):
    template_name = 'pages/project/project_members.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project_id = self.kwargs.get('project_id')
        try:
            if self.request.user.is_staff == True:
                project_data = GetProject.filter_id(id=project_id)
            else:
                project_data = GetProject.member(id=project_id, user=self.request.user)
            context['project_data'] = len(project_data)
            for data in project_data:
                context['project_id'] = data.id
                context['project_title'] = data.title
                context['project_password'] = data.password
                context['project_owner'] = data.owner
                context['project_members'] = data.members
                context['project_playbooks'] = data.playbooks
                context['project_inventories'] = data.inventories
                context['project_templates'] = data.templates
                context['user_list'] = CustomUser.objects.all()

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
def create_member(request):
    project_id = request.POST.get('project_id', '')
    user_id = request.POST.get('user_id', '')
    if project_id:
        try: 
            if request.user.is_staff:
                project = Project.objects.filter(id=project_id)
            else:
                project = GetProject.owner(id=project_id, owner=request.user)
            activity = GetProject.create_activity(project_id = project_id, user=request.user, description=f'USER #{request.user.id} added a new member to Project #{project_id}')
            member = GetProject.addMember(project_id = project_id, user_id=user_id)
            if member == False:
                return JsonResponse({'success': False, 'message': 'User not found'})
            return JsonResponse(
                    {
                        'success': True,
                        'member_id': member.id,
                        'member_username': member.username,
                        'member_email': member.email,
                        'member_first_name': member.first_name,
                        'member_last_name': member.last_name,
                    }
                )
            
        except Project.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'User not found'})

@csrf_exempt
@require_POST
@login_required
def delete_member(request, project_id, user_id):
    print(project_id)
    project_id = int(project_id)
    user_id = int(user_id)
    try:
        # Verifica se o usuário é o proprietário do projeto
        if request.user.is_staff:
            project = Project.objects.filter(id=project_id)
        else:
            project = GetProject.owner(id=project_id, owner=request.user)
        if project == False:
            return JsonResponse({'success': False, 'message': 'Without permission'})
        # REGISTER ACTIVITY
        try:
            user = CustomUser.objects.get(id=int(user_id))
        except:
            return JsonResponse({'success': False, 'message': 'User not found'})
        print(user.username)
        project[0].members.remove(user)
        activity = GetProject.create_activity(project_id = project_id, user=request.user, description=f'USER #{request.user.id} remove a member ID #{user_id} from project #{project_id}')

        return JsonResponse({'success': True, 'message': 'Member deleted.'})
    except Project.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Project not found'})