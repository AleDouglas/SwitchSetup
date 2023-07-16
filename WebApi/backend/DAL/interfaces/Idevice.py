from django.contrib import admin
from backend.DAL.models.device import *

class DeviceCredentialAdmin(admin.ModelAdmin):
    list_display = ('id','title')

admin.site.register(DeviceCredential, DeviceCredentialAdmin)