from django.contrib import admin
from backend.DAL.models.ansible import *

class PlaybookCustomAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'device')

admin.site.register(PlaybookCustom, PlaybookCustomAdmin)

class HostCustomAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'device')

admin.site.register(HostCustom, HostCustomAdmin)


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id','title')

admin.site.register(Task, TaskAdmin)