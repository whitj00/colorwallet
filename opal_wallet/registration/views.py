from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import logout as django_logout

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(form.cleaned_data['username'],
                                            None, form.cleaned_data['password1'])
            context = {'username':user.username}
            return render(request, 'registration/confirm.html', context)

    else:
        form = UserCreationForm()
    
    context = {'page_title':'Opal Color Wallet Registration', 'form':form}
    return render(request, 'registration/register.html', context)

def logout(request):
    django_logout(request)
    return redirect('/login')
