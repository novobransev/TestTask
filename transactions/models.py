from django.db import models
from wallet_app.models import AccountWallet
from django.core.exceptions import ValidationError


class Transactions(models.Model):
    sender = models.CharField(max_length=8)
    receiver = models.CharField(max_length=8)
    transfer_amount = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Количество денег на перевод', null=True)
    commision = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Комиcсия', null=True)
    status = models.BooleanField(blank=True, default=False)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None,  *args, **kwargs):
        """
            Здесь идет та самая транзакция
            Логика такова, чтобы совершить транзакцию, нужно получить id кошелька
            А дальше уже дело за малым
        """
        acc_sender = AccountWallet.objects.get(NAME=self.sender)
        acc_receiver = AccountWallet.objects.get(NAME=self.receiver)
        id_sender = AccountWallet.objects.filter(NAME=self.sender).values('id')[0]['id']
        id_receiver = AccountWallet.objects.filter(NAME=self.receiver).values('id')[0]['id']

        if int(AccountWallet.objects.filter(id=id_sender).values('currency_id')[0]['currency_id']) == int(AccountWallet.objects.filter(id=id_receiver).values('currency_id')[0]['currency_id'])\
                or int(AccountWallet.objects.filter(id=id_receiver).values('currency_id')[0]['currency_id']) == int(AccountWallet.objects.filter(id=id_sender).values('currency_id')[0]['currency_id']):

            if str(self.sender) == str(acc_sender):
                balance_sender = AccountWallet.objects.get(id=id_sender)
                bal1 = balance_sender.balance - self.transfer_amount
                balance_sender.balance = bal1
                balance_sender.save()

            if str(self.receiver) == str(acc_receiver):
                balance_receiver = AccountWallet.objects.get(id=id_receiver)
                bal2 = balance_receiver.balance + self.transfer_amount
                balance_receiver.balance = bal2
                balance_receiver.save()

            super(Transactions, self).save(*args, **kwargs)
        else:
            raise ValidationError('Валюты не совпадают, правильный перевод должен быть из RUB в RUB, из USD в USD')
