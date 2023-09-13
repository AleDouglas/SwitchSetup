from django.contrib import admin
from backend.DAL.models.ansible import *

class PlaybookCustomAdmin(admin.ModelAdmin):
    list_display = ('id','title')

admin.site.register(PlaybookCustom, PlaybookCustomAdmin)

class HostCustomAdmin(admin.ModelAdmin):
    list_display = ('id','title')

admin.site.register(HostCustom, HostCustomAdmin)