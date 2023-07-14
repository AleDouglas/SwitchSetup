from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from backend.forms import CustomUserCreationForm, CustomUserChangeForm

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