from django.db import models
from django.contrib.auth import get_user_model
from backend.lib.database.playbook import Playbook
from backend.lib.database.inventory import Inventory
from backend.lib.database.task import Task


class Template(models.Model):
    title = models.CharField("Title", max_length=150, blank=False, null=False)
    version = models.CharField("Version", max_length=10)
    date_time = models.DateTimeField("Date", auto_now_add=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='author_template')
    playbook = models.ForeignKey(Playbook, on_delete=models.CASCADE,related_name='templates')
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE,related_name='templates')
    tasks = models.ManyToManyField(Task,related_name='task_template')

    def __str__(self):
        return self.title
