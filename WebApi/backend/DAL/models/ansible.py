from django.db import models
import uuid

CISCO = 'Cisco'
HUAWEI = 'Huawei'
CHOICES = [
    (CISCO, "Cisco"),
    (HUAWEI, "Huawei"),
]


def unique_filename(instance, filename):
    if '.' in filename:
        ext = filename.split('.')[1]
        filename = f"{uuid.uuid4()}.{ext}"
        return f"backend/integrations/communs/custom/{filename}"
    else:
        filename = f"{uuid.uuid4()}.txt"
        return f"backend/integrations/communs/custom/{filename}"

class PlaybookCustom(models.Model):
    title = models.CharField("Title", max_length=150)
    about = models.TextField("About")
    playbook_file = models.FileField(upload_to=unique_filename)
    device = models.TextField("Device", default='None')
    SWITCH_CHOICES = CHOICES
    switch = models.CharField(max_length=10,choices=SWITCH_CHOICES,blank=False, null=False)

    def __str__(self):
        return self.title

class Command(models.Model):
    title = models.CharField("Title", max_length=150)
    description = models.TextField("Description")
    command = models.TextField("Command")
    SWITCH_CHOICES = CHOICES
    switch = models.CharField(max_length=10,choices=SWITCH_CHOICES,blank=False, null=False)

    def __str__(self):
        return self.title

class HostCustom(models.Model):
    title = models.CharField("Title", max_length=150,blank=False, null=False)
    about = models.TextField("About")
    host_file = models.FileField(upload_to=unique_filename)
    device = models.TextField("Device",blank=False, null=False)
    SWITCH_CHOICES = CHOICES
    switch = models.CharField(max_length=10,choices=SWITCH_CHOICES,blank=False, null=False)

    def __str__(self):
        return self.title

class Task(models.Model):
    title = models.CharField("Title", max_length=150,blank=False, null=False)
    about = models.TextField("About", default="Default about text") 
    host = models.ForeignKey(HostCustom, on_delete=models.CASCADE, blank=False, null=False) 
    playbook = models.ForeignKey(PlaybookCustom, on_delete=models.CASCADE, blank=False, null=False) 

    def __str__(self):
        return self.title