from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from backend.forms import CustomUserCreationForm, CustomUserChangeForm
from backend.lib.database import inventory
from backend.lib.database import playbook
from backend.lib.database import template
from backend.lib.database import dashboard
from backend.lib.database import project
from backend.lib.database import task
from backend.lib.database import key

CustomUser = get_user_model()

class CustomUserAdmin(UserAdmin):
	add_form = CustomUserCreationForm
	form = CustomUserChangeForm
	model = CustomUser
	list_display = ['email', 'username']
	fieldsets = (
		(None, {'fields': ('email', 'username','password',)}),
		('Informações Pessoais', {'fields':('first_name', 'last_name',)}),
		('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
		('Datas importantes', {'fields': ('last_login', 'date_joined')})
	)

admin.site.register(CustomUser, CustomUserAdmin)


class InventoryAdmin(admin.ModelAdmin):
	list_display = ('id','title')

class PlaybookAdmin(admin.ModelAdmin):
	list_display = ('id','title')

class ProjectAdmin(admin.ModelAdmin):
	list_display = ('id','title')

class ActivityAdmin(admin.ModelAdmin):
	list_display = ('id','description')

class TemplateAdmin(admin.ModelAdmin):
	list_display = ('id','title')

class TaskAdmin(admin.ModelAdmin):
	list_display = ('id','title')

class KeyAdmin(admin.ModelAdmin):
	list_display = ('id','name')

admin.site.register(inventory.Inventory, InventoryAdmin)
admin.site.register(playbook.Playbook, PlaybookAdmin)
admin.site.register(project.Project, ProjectAdmin)
admin.site.register(dashboard.Activity, ActivityAdmin)
admin.site.register(template.Template, TemplateAdmin)
admin.site.register(task.Task, TaskAdmin)
admin.site.register(key.Key, KeyAdmin)