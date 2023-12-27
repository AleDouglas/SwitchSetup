from django.db import models

class Playbook(models.Model):
    title = models.CharField("Title", max_length=150)
    description = models.TextField("description")
    date_time = models.DateTimeField("Date", auto_now_add=True)
    playbook_file = models.FileField(upload_to="backend/lib/ansible/playbooks/")

    def __str__(self):
        return self.title