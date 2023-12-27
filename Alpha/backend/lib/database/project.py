from django.db import models
from django.contrib.auth import get_user_model
from backend.lib.database.playbook import Playbook
from backend.lib.database.inventory import Inventory
from backend.lib.database.template import Template
from backend.lib.database.dashboard import Activity


class Project(models.Model):
    title = models.CharField("Title", max_length=150, blank=False, null=False)
    password = models.CharField("Password", max_length=15)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='owned_projects')
    members = models.ManyToManyField(get_user_model(), related_name='members_projects')
    playbooks = models.ManyToManyField(Playbook, related_name='playbook_project')
    inventories = models.ManyToManyField(Inventory, related_name='inventory_project')
    templates = models.ManyToManyField(Template, related_name='template_project')
    activity = models.ManyToManyField(Activity, related_name='activity_project')

    def __str__(self):
        return self.title
