# Generated by Django 4.0.2 on 2022-02-26 01:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_team_id_alter_team_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='participants',
            field=models.ManyToManyField(related_name='+', to=settings.AUTH_USER_MODEL),
        ),
    ]
