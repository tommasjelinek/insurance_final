# Generated by Django 4.1.6 on 2023-05-25 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insurance_app', '0027_users_produkt'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='attendees',
            new_name='doba_pojisteni',
        ),
    ]
