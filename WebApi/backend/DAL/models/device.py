from django.db import models


class DeviceCredential(models.Model):
    title = models.CharField("Title", max_length=60)
    username = models.CharField("Username", max_length=30)
    password = models.CharField("Password", max_length=30)
    

    def __str__(self):
        return self.title
