from django.forms import ModelForm
from wallet_app.models import AccountWallet


class WalletForm(ModelForm):
    class Meta:
        model = AccountWallet
        fields = ['id', 'name', 'wal_type', 'currency', 'balance', 'created_on', 'modified_on']
