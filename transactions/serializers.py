from rest_framework import serializers
from .models import Transactions


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = '__all__'
        read_only_fields = ('status', 'commision')  # эти поля он не редактирует, а только читает
