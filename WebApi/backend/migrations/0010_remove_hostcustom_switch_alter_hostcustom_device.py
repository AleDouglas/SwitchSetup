# Generated by Django 4.2.3 on 2023-10-26 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0009_alter_ansiblelog_options_alter_playbookcustom_switch'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hostcustom',
            name='switch',
        ),
        migrations.AlterField(
            model_name='hostcustom',
            name='device',
            field=models.TextField(default='10.0.0.0', verbose_name='Device'),
        ),
    ]