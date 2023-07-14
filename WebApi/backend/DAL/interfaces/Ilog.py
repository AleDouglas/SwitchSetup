from django.contrib import admin
from backend.DAL.models.log import *

class AnsibleLogAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'date')

admin.site.register(AnsibleLog, AnsibleLogAdmin)