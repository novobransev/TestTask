# Generated by Django 4.1.3 on 2022-12-05 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet_app', '0010_alter_accountwallet_name_alter_accountwallet_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountwallet',
            name='currency',
            field=models.CharField(max_length=3, null=True, verbose_name='Валюта счёта'),
        ),
        migrations.AlterField(
            model_name='accountwallet',
            name='wal_type',
            field=models.CharField(max_length=15, null=True, verbose_name='Тип счёта'),
        ),
    ]
