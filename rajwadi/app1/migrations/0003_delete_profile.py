# Generated by Django 4.2.1 on 2023-05-30 04:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_profile_delete_userprofile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]