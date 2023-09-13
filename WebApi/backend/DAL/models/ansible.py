from django.db import models
import uuid

def unique_filename(instance, filename):
    if '.' in filename:
        ext = filename.split('.')[1]
        filename = f"{uuid.uuid4()}.{ext}"
        return f"backend/integrations/communs/custom/{filename}"
    else:
        filename = f"{uuid.uuid4()}.txt"
        return f"backend/integrations/communs/custom/{filename}"

class PlaybookCustom(models.Model):
    title = models.CharField("Title", max_length=30)
    about = models.TextField("About")
    playbook_file = models.FileField(upload_to=unique_filename)

    def __str__(self):
        return self.title


class HostCustom(models.Model):
    title = models.CharField("Title", max_length=30)
    about = models.TextField("About")
    host_file = models.FileField(upload_to=unique_filename)

    def __str__(self):
        return self.title