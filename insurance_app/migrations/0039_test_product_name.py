# Generated by Django 4.1.6 on 2023-06-06 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insurance_app', '0038_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='product_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='insurance_app.product'),
        ),
    ]
