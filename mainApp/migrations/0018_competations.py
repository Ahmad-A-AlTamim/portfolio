# Generated by Django 5.0.7 on 2024-08-14 14:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0017_education_honorsandawards_imagesmodel_skills'),
    ]

    operations = [
        migrations.CreateModel(
            name='competations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.account')),
            ],
        ),
    ]
