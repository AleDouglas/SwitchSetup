from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
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
            context['project_key'] = project_data.key
        except Exception as e:
            print(f"Acesso negado: {e}")
        return context

    def render_to_response(self, context, **response_kwargs):
        if context['project_data'] == False:
            return redirect('home')
        return super().render_to_response(context, **response_kwargs)