# Generated by Django 4.1.6 on 2023-05-25 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insurance_app', '0015_users_attendees'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='attendees',
            new_name='pojisteni',
        ),
    ]
