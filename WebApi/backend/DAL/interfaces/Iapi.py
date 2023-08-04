from django.contrib import admin
from backend.DAL.models.api import *

class ApiKeyAdmin(admin.ModelAdmin):
    list_display = ('id','title')

admin.site.register(ApiKey, ApiKeyAdmin)