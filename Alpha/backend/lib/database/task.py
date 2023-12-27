from django.db import models
from django.contrib.auth import get_user_model


class Task(models.Model):
    CHOICES = [
        ('0', "Success"),
        ('1', "Running"),
        ('2', "Failed"),
        ('3', "Failed"),
        ('4', "Unreachable"),
    ]
    title = models.CharField("Title", max_length=150, blank=False, null=False)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='author_task')
    status = models.CharField(max_length=1, choices=CHOICES, blank=False, null=False, default='0')
    hour = models.DateTimeField("Date", auto_now_add=True)
    output = models.TextField("Output")

    def __str__(self):
        return self.title
