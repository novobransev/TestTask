# Generated by Django 4.1.3 on 2022-12-01 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='type',
            options={'verbose_name': 'Тип', 'verbose_name_plural': 'Типы'},
        ),
        migrations.AlterField(
            model_name='accountwallet',
            name='balance',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Баланс'),
        ),
    ]
