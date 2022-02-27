# Generated by Django 4.0.2 on 2022-02-27 15:45

import app.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_remove_goal_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='goal',
            name='team',
            field=models.OneToOneField(null=app.models.Team, on_delete=django.db.models.deletion.CASCADE, to='app.team'),
            preserve_default=app.models.Team,
        ),
    ]
