# Generated by Django 4.1.6 on 2023-05-22 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pojisteni',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zakladni', models.CharField(max_length=240)),
                ('cestovni', models.CharField(max_length=240)),
                ('havarijni', models.CharField(max_length=240)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=120)),
                ('last_name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254, verbose_name='User Email')),
                ('address', models.CharField(max_length=240)),
                ('phone', models.IntegerField(max_length=100)),
            ],
        ),
    ]
