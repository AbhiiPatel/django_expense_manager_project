# Generated by Django 4.2.3 on 2023-08-07 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_developer',
            new_name='is_user',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_manager',
        ),
    ]
