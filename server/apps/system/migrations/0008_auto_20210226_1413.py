# Generated by Django 3.0.7 on 2021-02-26 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0007_auto_20201214_0900'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dict',
            name='other',
        ),
        migrations.RemoveField(
            model_name='historicaldict',
            name='other',
        ),
    ]
