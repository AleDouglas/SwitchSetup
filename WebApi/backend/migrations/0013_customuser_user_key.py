# Generated by Django 4.2.3 on 2023-12-18 15:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0012_alter_command_switch_alter_hostcustom_device_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='user_key',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]