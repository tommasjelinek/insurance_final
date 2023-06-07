# Generated by Django 4.1.6 on 2023-06-08 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance_app', '0080_remove_usercontract_sjednane_usercontract_sjednane'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercontract',
            name='sjednane',
        ),
        migrations.AddField(
            model_name='usercontract',
            name='sjednane',
            field=models.ManyToManyField(blank=True, to='insurance_app.contract'),
        ),
    ]
