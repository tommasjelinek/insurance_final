# Generated by Django 4.1.6 on 2023-06-05 23:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insurance_app', '0034_rename_typ_pojisteni_pojisteni_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='hovno',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='insurance_app.product'),
        ),
    ]
