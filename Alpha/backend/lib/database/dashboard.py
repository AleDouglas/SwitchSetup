from django.db import models
from django.contrib.auth import get_user_model

# Registro de atividades
class Activity(models.Model):
    description = models.CharField("Description", max_length=150)
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True, related_name='dashboard')
    date_time = models.DateTimeField("Date", auto_now_add=True)

    def __str__(self):
        return self.description