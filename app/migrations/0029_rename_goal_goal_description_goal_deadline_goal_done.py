# Generated by Django 5.1 on 2024-08-23 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_remove_goal_owner_goal_team'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goal',
            old_name='goal',
            new_name='description',
        ),
        migrations.AddField(
            model_name='goal',
            name='deadline',
            field=models.DateField(null=True, verbose_name='Deadline'),
        ),
        migrations.AddField(
            model_name='goal',
            name='done',
            field=models.BooleanField(default=False, verbose_name='Done'),
        ),
    ]
