from django.urls import path, include
from .views import *
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'transaction', views.TransactionsViewSet)

urlpatterns = [
    path('wallet/transaction/', CreateTransactions.as_view(), name='create_transaction'),  # Создать транзакцию
    path('wallet/transaction/all/', ListTransactions.as_view(), name='all_transaction'),

    # API
    path('api/', include(router.urls)),
]
