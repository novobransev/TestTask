# Generated by Django 4.1.3 on 2022-12-05 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallet_app', '0011_alter_accountwallet_currency_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountwallet',
            name='currency',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='wallet_app.currency', verbose_name='Валюта счёта'),
        ),
        migrations.AlterField(
            model_name='accountwallet',
            name='wal_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='wallet_app.type', verbose_name='Тип счёта'),
        ),
    ]
