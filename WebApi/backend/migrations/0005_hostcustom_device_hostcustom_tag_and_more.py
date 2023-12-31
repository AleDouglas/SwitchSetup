# Generated by Django 4.2.3 on 2023-10-18 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_rename_host_file_playbookcustom_playbook_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostcustom',
            name='device',
            field=models.TextField(default='None', verbose_name='Device'),
        ),
        migrations.AddField(
            model_name='hostcustom',
            name='tag',
            field=models.TextField(default='None', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='playbookcustom',
            name='device',
            field=models.TextField(default='None', verbose_name='Device'),
        ),
        migrations.AddField(
            model_name='playbookcustom',
            name='tag',
            field=models.TextField(default='None', verbose_name='Tags'),
        ),
    ]
