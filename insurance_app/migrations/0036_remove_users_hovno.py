# Generated by Django 4.1.6 on 2023-06-05 23:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insurance_app', '0035_users_hovno'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='hovno',
        ),
    ]
