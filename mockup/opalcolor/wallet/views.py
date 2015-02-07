from django.template import loader
from django.shortcuts import render

# @login_required
def index(request):
    context = {'page_title':'Index Page'}
    return render(request, 'wallet/index.html', context)

def account(request):
    context = {'page_title':'Accounts'}
    return render(request, 'wallet/account.html', context)

def send(request):
    context = {'page_title':'Send Money'}
    return render(request, 'wallet/send.html', context)

def transactions(request):
    context = {'page_title':'Transactions'}
    return render(request, 'wallet/transactions.html', context)

def assets(request):
    context = {'page_title':'Index Page'}
    return render(request, 'wallet/assets.html', context)


