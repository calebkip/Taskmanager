# Generated by Django 4.2.7 on 2024-01-09 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tasks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='technician',
            name='tickets',
        ),
    ]
