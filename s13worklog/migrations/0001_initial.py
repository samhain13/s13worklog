# Generated by Django 2.0 on 2018-04-21 09:16

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
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LogItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_dt', models.DateTimeField(blank=True, null=True, verbose_name='Start Date and Time')),
                ('end_dt', models.DateTimeField(blank=True, null=True, verbose_name='End Date and Time')),
                ('notes', models.TextField(blank=True, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Log Items',
                'verbose_name': 'Log Item',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('done', models.BooleanField(default=False)),
                ('categories', models.ManyToManyField(to='s13worklog.Category')),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Assigned Users')),
            ],
        ),
        migrations.AddField(
            model_name='logitem',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='s13worklog.Task'),
        ),
    ]
