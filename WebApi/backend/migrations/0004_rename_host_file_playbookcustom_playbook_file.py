# Generated by Django 4.2.3 on 2023-09-12 23:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_hostcustom_playbookcustom'),
    ]

    operations = [
        migrations.RenameField(
            model_name='playbookcustom',
            old_name='host_file',
            new_name='playbook_file',
        ),
    ]