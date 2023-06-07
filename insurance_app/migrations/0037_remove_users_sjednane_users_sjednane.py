# Generated by Django 4.1.6 on 2023-06-06 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance_app', '0036_remove_users_hovno'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='sjednane',
        ),
        migrations.AddField(
            model_name='users',
            name='sjednane',
            field=models.ManyToManyField(blank=True, to='insurance_app.pojisteni'),
        ),
    ]