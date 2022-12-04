from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from transactions.models import Transactions
from wallet_app.models import AccountWallet


class CreateTransactions(CreateView):
    model = Transactions
    template_name = 'wallet_app/create_transaction.html'
    fields = ['sender', 'receiver', 'transfer_amount']
    success_url = reverse_lazy('home')
    all_sender = AccountWallet.objects.all()

    def form_valid(self, form):
        instance = form.save(commit=False)
        print(self.all_sender)
        for i in list(self.all_sender):
            if str(instance.sender) == str(i):
                instance.status = True
                print('YES')
                return super().form_valid(form)
            else:
                print('NO')


class ListTransactions(ListView):
    model = Transactions
    template_name = 'wallet_app/all_transactions.html'
