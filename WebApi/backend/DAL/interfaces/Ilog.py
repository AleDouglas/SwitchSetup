from django.contrib import admin
from backend.DAL.models.log import *

class AnsibleLogAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'service', 'data')

admin.site.register(AnsibleLog, AnsibleLogAdmin)