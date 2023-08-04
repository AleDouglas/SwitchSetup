from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from backend.views.utils import AdminRequired
from backend.DAL.DAO.apiDAO import *
from backend.DAL.models.api import ApiKey

class ApiPageView(AdminRequired, TemplateView):
    template_name = 'api.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['settings'] = 0
        context['keys'] = getAllApi()
        context['page'] = "Manage Keys"
        return context

    def post(self, request ,*args, **kwargs):
        createKey(
            title = request.POST.get('title'),
        )
        result = "The key have been successfully upgraded."
        return self.render_to_response(self.get_context_data(result = result))

class ApiDeleteView(AdminRequired, DeleteView):
    template_name = 'api.html'
    model = ApiKey
    success_url = reverse_lazy("apiKey")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['settings'] = 1
        context['page'] = "Delete Key"
        return context