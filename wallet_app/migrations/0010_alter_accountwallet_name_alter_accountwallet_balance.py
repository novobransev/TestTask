# Generated by Django 4.1.3 on 2022-12-04 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet_app', '0009_rename_name_accountwallet_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountwallet',
            name='NAME',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='accountwallet',
            name='balance',
            field=models.DecimalField(decimal_places=2, max_digits=20, null=True, verbose_name='Баланс'),
        ),
    ]
