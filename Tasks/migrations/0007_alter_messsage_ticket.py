# Generated by Django 4.2.7 on 2024-01-13 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tasks', '0006_remove_ticket_message_messsage_ticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messsage',
            name='ticket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='Tasks.ticket'),
        ),
    ]
