from django.urls import path, include
from backend.lib.views.project import ProjectView, create_project, delete_project
from backend.lib.views.dashboard import DashboardView
from backend.lib.views.inventory import InventoryView, create_inventory, delete_inventory
from backend.lib.views.playbook import PlaybookView, create_playbook, delete_playbook
from backend.lib.views.template import TaskTemplateView, create_template, delete_template, execute_template
from backend.lib.views.members import MembersView, create_member, delete_member
from backend.lib.views.task import TaskView, get_task
from backend.lib.views.admin_area import AdminAreaView, delete_user
urlpatterns = [
    path('', ProjectView.as_view(), name='home'),
    path('create_project/', create_project, name='create_project'),
    path('delete_project/<int:project_id>/', delete_project, name='delete_project'),

    path('project/dashboard/<int:project_id>/', DashboardView.as_view(), name='dashboard'),

    path('project/inventory/<int:project_id>/', InventoryView.as_view(), name='inventory'),
    path('create_inventory/', create_inventory, name='create_inventory'),
    path('delete_inventory/<int:project_id>/<int:inventory_id>', delete_inventory, name='delete_inventory'),

    path('project/playbook/<int:project_id>/', PlaybookView.as_view(), name='playbook'),
    path('create_playbook/', create_playbook, name='create_playbook'),
    path('delete_playbook/<int:project_id>/<int:playbook_id>', delete_playbook, name='delete_playbook'),

    path('project/template/<int:project_id>/', TaskTemplateView.as_view(), name='template'),
    path('create_template/', create_template, name='create_template'),
    path('delete_template/<int:project_id>/<int:template_id>', delete_template, name='delete_template'),
    path('execute_template/<int:project_id>/<int:template_id>', execute_template, name='execute_template'),

    path('project/task/<int:project_id>/<int:template_id>/', TaskView.as_view(), name='task'),
    path('get_task/<int:task_id>', get_task, name='get_task'),



    path('project/members/<int:project_id>/', MembersView.as_view(), name='members'),
    path('create_member/', create_member, name='create_member'),
    path('delete_member/<int:project_id>/<int:user_id>', delete_member, name='delete_member'),

    path('admin_area', AdminAreaView.as_view(), name='admin_area'),
    path('admin_area/delete_user/<int:user_id>/', delete_user, name='delete_user'),


]