# Generated by Django 4.1.6 on 2023-05-25 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insurance_app', '0018_remove_produkty_notes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='pridat_pojisteni',
        ),
    ]
