# Generated by Django 4.1.3 on 2022-12-04 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallet_app', '0007_rename_name_accountwallet__name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accountwallet',
            old_name='_name',
            new_name='name',
        ),
    ]