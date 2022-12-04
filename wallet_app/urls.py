from django.urls import path
from .views import *

urlpatterns = [
    path('create/', WalletCreate.as_view(), name='create'),
    path('wallets/', GetAllWallet.as_view(), name='all_wallet'),
    path('wallets/<slug:slug>/', DeleteWallet.as_view(), name='delete_wallet'),
    path('', home, name='home')
]
