import uuid
from django.db import models

class Key(models.Model):
    key = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    add_inventory = models.BooleanField(default=False)
    add_playbook = models.BooleanField(default=False)
    add_template = models.BooleanField(default=False)
    execute_template = models.BooleanField(default=True)
    remove_itens = models.BooleanField(default=False)

