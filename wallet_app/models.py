from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models


class Currency(models.Model):
    title = models.CharField(max_length=50, db_index=True, verbose_name="Наименование валюты")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Валюта"
        verbose_name_plural = "Валюты"


class Type(models.Model):
    wallet_type = models.CharField(max_length=50, db_index=True, verbose_name="Тип")

    def __str__(self):
        return self.wallet_type

    class Meta:
        verbose_name = "Тип"
        verbose_name_plural = "Типы"


class AccountWallet(models.Model):
    NAME = models.CharField(max_length=8)
    wal_type = models.ForeignKey(Type, on_delete=models.PROTECT, null=True, verbose_name="Тип счёта")
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT, null=True, verbose_name="Валюта счёта")
    balance = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Баланс', null=True)
    owner = models.ForeignKey(User, on_delete=models.PROTECT, null=True, verbose_name='Владелец счёта', blank=True)
    created_on = models.DateTimeField(auto_now_add=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True, auto_now=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None, *args, **kwargs):
        """Здесь идет проверка на количество кошельков"""

        if int(AccountWallet.objects.filter(owner=self.owner).count()) <= 4:
            super(AccountWallet, self).save(*args, **kwargs)
        else:
            raise ValidationError('Превышено количество кошельков, максимум возможно 5 штук')

    def __str__(self):
        return self.NAME
