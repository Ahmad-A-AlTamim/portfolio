# Generated by Django 5.0.7 on 2024-08-14 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0019_account_pdfcv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='pdfCV',
            field=models.FileField(upload_to='pdf/%Y/%m/%d/%H/%M/%S/', verbose_name='PDF CV'),
        ),
    ]
