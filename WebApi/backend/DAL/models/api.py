from django.db import models


class ApiKey(models.Model):
    title = models.CharField("Title", max_length=60)
    key = models.CharField("Username", max_length=100, editable=False)
    

    def __str__(self):
        return self.title
