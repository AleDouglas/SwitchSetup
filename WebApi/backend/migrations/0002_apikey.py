# Generated by Django 4.2.3 on 2023-07-23 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApiKey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='Title')),
                ('key', models.CharField(editable=False, max_length=100, verbose_name='Username')),
            ],
        ),
    ]