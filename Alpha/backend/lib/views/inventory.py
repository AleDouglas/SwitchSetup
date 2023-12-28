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

class InventoryView(LoginRequiredMixin, TemplateView):
    template_name = 'pages/project/project_inventory.html'

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
            print("Access problem")
            return redirect('home')
        return super().render_to_response(context, **response_kwargs)



@csrf_exempt
@require_POST
@login_required
def create_inventory(request):
    project_id = request.POST.get('project_id', '')
    title = request.POST.get('title', '')
    description = request.POST.get('description', '')
    inventory_file = request.FILES.get('inventory_file', None)

    if project_id:
        try:
            # Verifica se o usuário é o proprietário do projeto
            project_data = GetProject.owner(id=project_id, owner=request.user)
            inventory = GetProject.create_inventory(title=title, description=description, inventory_file=inventory_file)
            project_data.inventories.add(inventory)
            # REGISTER ACTIVITY
            activity = GetProject.create_activity(project_id = project_id, user=request.user, description=f'USER #{request.user.id} added a new inventory #{inventory.id}')
            return JsonResponse(
                    {
                        'success': True, 
                        'inventory_id': inventory.id, 
                        'inventory_title': inventory.title,
                        'inventory_description': inventory.description,
                        'inventory_time': inventory.date_time,
                    }
                )
            
        except:
            return JsonResponse({'success': False, 'message': 'Inventory or proejct not found.'})


@csrf_exempt
@require_POST
@login_required
def delete_inventory(request, project_id, inventory_id):
    try:
        project = GetProject.owner(id=project_id, owner=request.user)
        inventory = project.inventories.get(id=inventory_id)
        if inventory == False:
            return JsonResponse({'success': False, 'message': 'Inventory not found'})
        activity = GetProject.create_activity(project_id = project_id, user=request.user, description=f'USER #{request.user.id} delete inventory #{inventory.id}')
        project.inventories.remove(inventory)
        return JsonResponse({'success': True, 'message': 'Inventory delete successfully'})
    except:
        return JsonResponse({'success': False, 'message': 'Inventory or project not found'})



