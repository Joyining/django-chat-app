# Generated by Django 4.1.7 on 2023-04-11 08:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(default='', max_length=10000)),
                ('timestamp', models.DateTimeField(default=datetime.datetime)),
                ('user_name', models.CharField(default='', max_length=100)),
                ('room', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Untitled Room', max_length=100)),
            ],
        ),
    ]
