from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from wallet.forms import OpalSendForm
from wallet_functions import wallet_functions

@login_required
def index(request):
    context = {'page_title':'Index Page'}
    return render(request, 'wallet/index.html', context)

@login_required
def update(request):
    wallet_functions.update_stats(request.user)
    return redirect(index)

@login_required
def account(request):
    accounts = wallet_functions.list_unspent()
    context = {'page_title':'Accounts', 'accounts':accounts}
    return render(request, 'wallet/account.html', context)

@login_required
def send(request):
    if request.method == 'POST':
        form = OpalSendForm(request.POST)
        if form.is_valid():
            status = wallet_functions.send_opal(form.cleaned_data)
            if status == 0:
                return redirect(transactions)
            else:
                context = {'error':'Invalid transaction.', 'form':form, 'page_title':'Send Money'}
                return render(request, 'wallet/send.html', context)
    else:
        form = OpalSendForm(initial={'from_address': 'Main account'})

    context = {'page_title':'Send Money', 'form':form}
    return render(request, 'wallet/send.html', context)

@login_required
def transactions(request):
    txs = wallet_functions.list_transactions()
    context = {'page_title':'Transactions', 'txs':txs}
    return render(request, 'wallet/transactions.html', context)

@login_required
def assets(request):
    context = {'page_title':'Index Page'}
    return render(request, 'wallet/assets.html', context)


