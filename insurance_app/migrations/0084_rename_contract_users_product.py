# Generated by Django 4.1.6 on 2023-06-08 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insurance_app', '0083_alter_users_contract'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='contract',
            new_name='product',
        ),
    ]
