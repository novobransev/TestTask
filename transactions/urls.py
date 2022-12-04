from django.urls import path
from .views import *

urlpatterns = [
    path('wallet/transaction/', CreateTransactions.as_view(), name='create_transaction'),  # Создать транзакцию
    path('wallet/transaction/all/', ListTransactions.as_view(), name='all_transaction')  # Создать транзакцию
]
