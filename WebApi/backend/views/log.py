from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from backend.DAL.DAO.logDAO import getLog
from backend.views.utils import AdminRequired

class LogView(AdminRequired, TemplateView):
    template_name = 'log.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['log_list'] = getLog()
        return context