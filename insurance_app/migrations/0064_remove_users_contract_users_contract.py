# Generated by Django 4.1.6 on 2023-06-08 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance_app', '0063_remove_users_attendees_users_contract'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='contract',
        ),
        migrations.AddField(
            model_name='users',
            name='contract',
            field=models.ManyToManyField(blank=True, null=True, to='insurance_app.contract'),
        ),
    ]
