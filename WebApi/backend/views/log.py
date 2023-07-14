from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from backend.DAL.DAO.logDAO import filterLog

class LogView(LoginRequiredMixin, TemplateView):
    template_name = 'log.html'

    def post(self, request ,*args, **kwargs):
        logs = filterLog(
            id= request.POST['id'],
            user=request.POST['username'],
            date=request.POST['date'].replace('/', '-'),

        )
        return render(request, self.template_name, {'logs': logs, 'search': 1})