# Generated by Django 4.1.6 on 2023-06-08 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insurance_app', '0078_remove_usercontract_uzivatel_usercontract_uzivatel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercontract',
            name='uzivatel',
        ),
        migrations.AddField(
            model_name='usercontract',
            name='uzivatel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='insurance_app.users'),
        ),
    ]
