# Django import
from django.shortcuts import render, redirect
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

# PÁGINA PRINCIPAL DO PROJETO
class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'pages/project/project_dashboard.html'

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
            context['project_activity'] = project_data.activity

        except Exception as e:
            context['project_data'] = False
            print(f"Acesso negado: {e}")
        return context

    def render_to_response(self, context, **response_kwargs):

        if context['project_data'] == False:
            return redirect('home')
        return super().render_to_response(context, **response_kwargs)


