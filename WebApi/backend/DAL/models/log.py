from django.db import models

class AnsibleLog(models.Model):
    user = models.CharField("Username", max_length=30, null=False, blank=False)
    service = models.TextField("Service", default='New DB')
    description = models.TextField("Description", default='New DB')
    data = models.CharField("Data", max_length=10, default='New DB')
    hour = models.CharField("Hour", max_length=10, default='New DB')
    host = models.TextField("Host", default='New DB')
    playbook = models.TextField("Playbook", default='New DB')
    output = models.TextField("Output", default='New DB')

    def __str__(self):
        return self.service