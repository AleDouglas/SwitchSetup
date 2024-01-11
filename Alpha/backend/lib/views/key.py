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


class KeyView(LoginRequiredMixin, TemplateView):
    template_name = 'pages/project/project_key.html'

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
            context['project_key'] = project_data.key.all
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
def create_key(request):
    project_id = request.POST.get('project_id', '')
    title = request.POST.get('title', '')
    add_inventory = request.POST.get('add_inventory', '').lower()
    add_playbook = request.POST.get('add_playbook', '').lower()
    add_template = request.POST.get('add_template', '').lower()
    remove_items = request.POST.get('remove_items', '').lower()



    add_inventory = add_inventory == 'true'
    add_playbook = add_playbook == 'true'
    add_template = add_template == 'true'
    remove_items = remove_items == 'true'

    if project_id:
        try: 
            if request.user.is_staff:
                project = Project.objects.get(id=project_id)
            else:
                project = GetProject.owner(id=project_id, owner=request.user)
            key = GetProject.create_key(project = project, title=title, add_inventory=add_inventory, add_playbook=add_playbook, add_template=add_template, remove_items=remove_items)
            activity = GetProject.create_activity(project = project, user=request.user, description=f'USER #{request.user.id} added a new key #{key.id} to Project #{project_id}')
            if key == False:
                return JsonResponse({'success': False, 'message': 'Error to create Key'})
            return JsonResponse(
                    {
                        'success': True,
                        'key_id': key.id,
                        'key': key.key,
                        'key_title': key.name,
                        'key_inventory': key.add_inventory,
                        'key_playbook': key.add_playbook,
                        'key_template': key.add_template,
                        'key_remove': key.remove_itens,
                    }
                )
            
        except:
            return JsonResponse({'success': False, 'message': 'Error to create Key'})
    else:
        return JsonResponse({'sucess': False, 'message': 'Error to create Key'})