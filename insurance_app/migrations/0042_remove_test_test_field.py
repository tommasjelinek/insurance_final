# Generated by Django 4.1.6 on 2023-06-06 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insurance_app', '0041_remove_users_sjednane_test_users_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='test_field',
        ),
    ]