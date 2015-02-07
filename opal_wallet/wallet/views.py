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

def account(request):
    context = {'page_title':'Accounts'}
    return render(request, 'wallet/account.html', context)

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

    accounts = wallet_functions.list_accounts()
    context = {'page_title':'Send Money', 'form':form}
    return render(request, 'wallet/send.html', context)

def transactions(request):
    context = {'page_title':'Transactions'}
    return render(request, 'wallet/transactions.html', context)

def assets(request):
    context = {'page_title':'Index Page'}
    return render(request, 'wallet/assets.html', context)


