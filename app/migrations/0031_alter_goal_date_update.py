# Generated by Django 5.1 on 2024-08-23 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0030_goal_date_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='date_update',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Update'),
        ),
    ]
