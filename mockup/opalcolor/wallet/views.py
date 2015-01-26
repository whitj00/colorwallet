from django.template import loader
from django.shortcuts import render

def index(request):
    context = {'page_title':'Index Page'}
    return render(request, 'wallet/index.html', context)


