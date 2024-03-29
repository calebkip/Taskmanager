# Generated by Django 4.2.7 on 2024-01-09 17:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Caller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Technician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tasks.department')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('priority', models.CharField(blank=True, choices=[('level 1', 'Critical'), ('level 3', 'Escalated'), ('level 5', 'Normal')], max_length=20, null=True)),
                ('resolved', models.CharField(blank=True, choices=[('resolved', 'Critical'), ('on hold', 'Escalated'), ('awaiting more info', 'Normal')], max_length=30, null=True)),
                ('open_status', models.BooleanField(default=True)),
                ('assigned', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='technicianassigned', to='Tasks.technician')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Tasks.category')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tasks.caller')),
            ],
        ),
        migrations.AddField(
            model_name='technician',
            name='tickets',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Tasks.ticket'),
        ),
        migrations.AddField(
            model_name='technician',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Messsage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('commeter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tasks.ticket')),
            ],
        ),
        migrations.AddField(
            model_name='department',
            name='supervisor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tasks.supervisor'),
        ),
        migrations.AddField(
            model_name='caller',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tasks.department'),
        ),
        migrations.AddField(
            model_name='caller',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
