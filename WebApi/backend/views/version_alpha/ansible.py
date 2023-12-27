from backend.DAL.DAO.ansibleDAO import GetPlaybook, GetHost, GetAnsibleSetting
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class TaskView(LoginRequiredMixin, TemplateView):
    pass