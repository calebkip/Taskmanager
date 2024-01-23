# Generated by Django 4.2.7 on 2024-01-13 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tasks', '0005_rename_messages_ticket_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='message',
        ),
        migrations.AddField(
            model_name='messsage',
            name='ticket',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='Tasks.ticket'),
            preserve_default=False,
        ),
    ]
