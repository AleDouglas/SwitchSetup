from django.db import models

class AnsibleLog(models.Model):
    user = models.CharField("Username", max_length=30, null=False, blank=False)
    date = models.CharField("Date", max_length=10, null=False, blank=False)
    hour = models.CharField("Hour", max_length=10, null=False, blank=False)
    switch = models.CharField("Switch", max_length=10, null=False, blank=False)
    host = models.TextField("Hosts", null=False, blank=False)
    playbook = models.TextField("Playbook", null=False, blank=False)
    output = models.TextField("Output", null=False, blank=False)

    class Meta :
        ordering = ['-id']

    def __str__(self):
        return self.user