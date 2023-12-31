# Generated by Django 4.2.3 on 2023-10-27 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0011_hostcustom_switch_alter_hostcustom_device'),
    ]

    operations = [
        migrations.AlterField(
            model_name='command',
            name='switch',
            field=models.CharField(choices=[('Cisco', 'Cisco'), ('Huawei', 'Huawei')], max_length=10),
        ),
        migrations.AlterField(
            model_name='hostcustom',
            name='device',
            field=models.TextField(verbose_name='Device'),
        ),
        migrations.AlterField(
            model_name='hostcustom',
            name='switch',
            field=models.CharField(choices=[('Cisco', 'Cisco'), ('Huawei', 'Huawei')], max_length=10),
        ),
        migrations.AlterField(
            model_name='playbookcustom',
            name='switch',
            field=models.CharField(choices=[('Cisco', 'Cisco'), ('Huawei', 'Huawei')], max_length=10),
        ),
    ]
