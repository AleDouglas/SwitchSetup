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
from backend.lib.database.task import Task

# Methods
from backend.lib.methods.project import GetProject

class TaskView(LoginRequiredMixin, TemplateView):
    template_name = 'pages/project/project_task.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project_id = self.kwargs.get('project_id')
        template_id = self.kwargs.get('template_id')
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

            # GET TASK INFORMATIONS
            template = data.templates.get(id=int(template_id))
            context['template'] = template
            context['task_list'] = template.tasks.all()

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
def get_task(request, task_id):
    try:
        task_id = int(task_id)
        get_task = GetProject.get_task(id=task_id)
        get_date = str(get_task.hour)
        return JsonResponse(
            {
                'success': True,
                'task_id': get_task.id,
                'task_title': get_task.title,
                'task_author_first_name': get_task.author.first_name,
                'task_author_last_name': get_task.author.last_name,
                'task_status': get_task.status,
                'task_date': datetime.strptime(get_date, "%Y-%m-%d %H:%M:%S.%f%z").strftime("%Y-%m-%d %I:%M:%S %p"),
                'task_output': get_task.output,
            }
        )
    except ValueError:
        return JsonResponse({'success': False, 'message': 'Invalid task_id format'})
    except Exception as e:
        print(e)
        return JsonResponse({'success': False, 'message': 'Task not found'})

