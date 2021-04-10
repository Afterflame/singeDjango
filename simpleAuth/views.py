from mainapp.views import home
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout as logout_req
from simpleAuth.forms import RegisterForm


def loglogout(request):
    logout_req(request)
    return redirect('login')


def registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            try :
                user = form.save()
                user.refresh_from_db()
                user.save()
                raw_password = form.cleaned_data.get('password1')
            except :
                form = RegisterForm()
                return render(request, 'simpleAuth/register.html', {'form': form})
            user = authenticate(password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'simpleAuth/register.html', {'form': form})

# Create your views here.
