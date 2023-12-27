from django.db import models

class Inventory(models.Model):
    title = models.CharField("Title", max_length=150)
    description = models.TextField("description")
    date_time = models.DateTimeField("Date", auto_now_add=True)
    inventory_file = models.FileField(upload_to="backend/lib/ansible/inventory/")

    def __str__(self):
        return self.title