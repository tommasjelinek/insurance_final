# Generated by Django 4.1.6 on 2023-06-06 22:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insurance_app', '0052_users_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='product',
        ),
    ]