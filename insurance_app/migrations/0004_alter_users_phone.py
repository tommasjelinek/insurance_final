# Generated by Django 4.1.6 on 2023-05-22 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance_app', '0003_pojisteni_pojistenci'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='phone',
            field=models.IntegerField(verbose_name=100),
        ),
    ]
