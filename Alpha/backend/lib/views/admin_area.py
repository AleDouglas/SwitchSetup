# Django import
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Database
from backend.lib.database.user import CustomUser
from backend.lib.database.task import Task
from backend.lib.database.dashboard import Activity
# Methods
from backend.lib.methods.project import GetProject
# Form
from backend.forms import CustomUserCreationForm


class AdminAreaView(LoginRequiredMixin, TemplateView):
    template_name = 'pages/project/project_admin_area.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_list'] = CustomUser.objects.all()
        context['project_list'] = GetProject.all()
        context['task_list'] = GetProject.all_task()
        context['activity_list'] = Activity.objects.order_by('-id')

        context['user_len'] = len(context['user_list'])
        context['project_len'] = len(context['project_list'])
        context['task_len'] = len(context['task_list'])

        context['form'] = CustomUserCreationForm()
        return context


    def render_to_response(self, context, **response_kwargs):
        if self.request.user.is_staff == False:
            return redirect('home')
        return super().render_to_response(context, **response_kwargs)

    def post(self, request ,*args, **kwargs):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            activity = GetProject.create_activity(user=request.user, description=f'Admin #{self.request.user.id} create a new user #{user.id}')
            context = self.get_context_data()

            return render(request, self.template_name, context)
        else:
            context['create_result'] = 'Failed to create a user'
            return render(request, self.template_name, context)


@csrf_exempt
@require_POST
@login_required
def delete_user(request, user_id):
    try:
        if request.user.is_staff:
            user = CustomUser.objects.get(id=int(user_id))
            if len(CustomUser.objects.filter(is_staff=True)) < 2:
                return JsonResponse({'success': False, 'result_user': 'Problem deleting user: Make sure there is more than one admin account on the system'})
            activity = GetProject.create_activity(user=request.user, description=f'Admin #{request.user.id} delete user ID #{user_id}')
            user.delete()
            return JsonResponse({'success': True, 'result_user': 'User deleted successfully'})
        else:
            return JsonResponse({'success': False, 'result_user': 'Access denied'})
    except CustomUser.DoesNotExist:
        return JsonResponse({'success': False, 'result_user': 'User not found'})

