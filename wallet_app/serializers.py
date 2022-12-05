from rest_framework import serializers

from .models import AccountWallet


class WalletSerializer(serializers.ModelSerializer):

    class Meta:
        model = AccountWallet
        fields = ('id', 'NAME', 'wal_type', 'currency', 'balance', 'created_on', 'modified_on')
        read_only_fields = ('NAME', 'balance', 'slug', 'owner')  # эти поля он не редактирует, а только читает

    def to_representation(self, instance):  # Как я понял, этот метод позволяет более точно увидеть все данные
        """Позволяет убрать такую логическую ошибку, как вывод не id, а именно имя пользователя"""

        rep = super(WalletSerializer, self).to_representation(instance)
        rep['wal_type'] = str(instance.wal_type).capitalize()
        rep['currency'] = str(instance.currency).upper()
        return rep
