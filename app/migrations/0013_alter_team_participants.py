# Generated by Django 4.0.2 on 2022-02-26 18:02

import app.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_team_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='participants',
            field=models.ManyToManyField(default=app.models.CustomUser, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
    ]
