# Generated by Django 4.2.7 on 2024-01-09 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='profile_picture',
            new_name='picture',
        ),
    ]
