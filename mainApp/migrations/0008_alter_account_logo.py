# Generated by Django 5.0.7 on 2024-08-07 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0007_account_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='logo',
            field=models.ImageField(upload_to='images/logo/%Y/%m/%d/%H/%M/%S/', verbose_name='Logo'),
        ),
    ]
