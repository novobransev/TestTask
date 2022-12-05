import random
import string
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from .serializers import WalletSerializer
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView
from wallet_app.models import AccountWallet


class WalletCreate(LoginRequiredMixin, CreateView):
    model = AccountWallet
    fields = ['wal_type', 'currency']
    template_name = 'wallet_app/create.html'
    success_url = reverse_lazy('home')

    @staticmethod
    def get_random_name():
        """Создаем имя кошельку из букв английского алфавита и цифр"""
        letters = list(string.ascii_lowercase) + list(string.ascii_uppercase)
        numbers = [str(num) for num in range(10)]
        all_list = letters + numbers
        word = ''

        for value in range(8):
            word += random.choice(all_list)

        return word

    def form_valid(self, form):
        """
            Тут мы добавляем автоматически пользователя к записи
            А также делаем проверку насчет записей пользователя
        """
        instance = form.save(commit=False)
        if int(instance.currency.pk) == 3:
            instance.balance = 100
        else:
            instance.balance = 3
        random_word = self.get_random_name()
        instance.slug = random_word
        instance.NAME = random_word
        instance.owner = self.request.user

        return super().form_valid(form)


class GetAllWallet(LoginRequiredMixin, ListView):
    model = AccountWallet
    template_name = 'wallet_app/all_wallet.html'

    def get_queryset(self):
        """Тут получаем все кошельки от определенного пользователя"""
        return self.model.objects.filter(owner=self.request.user)


class DeleteWallet(LoginRequiredMixin, DeleteView):
    model = AccountWallet
    template_name = 'wallet_app/confirm.html'
    success_url = reverse_lazy('home')


class WalletViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = AccountWallet.objects.all()
    serializer_class = WalletSerializer
    lookup_field = 'NAME'  # Позволяет получить экземпляр, не по id, а по полю NAME

    def perform_create(self, serializer):
        random_name = WalletCreate.get_random_name()
        serializer.validated_data['NAME'] = random_name

        if str(serializer.validated_data.get('currency')) == 'RUB':
            serializer.validated_data['balance'] = 100
        else:
            serializer.validated_data['balance'] = 3
        serializer.validated_data['owner'] = self.request.user  # Здесь почему-то присваивается число, а не имя

        print(serializer.validated_data.get('owner'))  # Тут увидим имя пользователя
        serializer.save()


def home(request):
    return render(request, 'wallet_app/home.html')
