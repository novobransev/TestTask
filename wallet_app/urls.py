from .views import *
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'wallets', views.WalletViewSet)


urlpatterns = [
    path('create/', WalletCreate.as_view(), name='create'),
    path('wallets/', GetAllWallet.as_view(), name='all_wallet'),
    path('wallets/<slug:slug>/', DeleteWallet.as_view(), name='delete_wallet'),
    path('', home, name='home'),

    # API
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
