# Generated by Django 4.2.3 on 2023-09-12 23:50

import backend.DAL.models.ansible
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_apikey'),
    ]

    operations = [
        migrations.CreateModel(
            name='HostCustom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Title')),
                ('about', models.TextField(verbose_name='About')),
                ('host_file', models.FileField(upload_to=backend.DAL.models.ansible.unique_filename)),
            ],
        ),
        migrations.CreateModel(
            name='PlaybookCustom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Title')),
                ('about', models.TextField(verbose_name='About')),
                ('host_file', models.FileField(upload_to=backend.DAL.models.ansible.unique_filename)),
            ],
        ),
    ]
