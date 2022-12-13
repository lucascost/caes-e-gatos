from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from account.forms import UserForm, UserLoginForm
from core.forms import PerfilForm


def try_auth(request, email, password):
    result = authenticate(request, email=email, password=password)
    if result is not None:
        login(request, result)
        return True
    return False

def user_login(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')

    return render(request, 'auth/login.html', {'form':UserLoginForm})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def user_signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = UserForm(request.POST)
        perfil_form = PerfilForm(request.POST)
        if form.is_valid() and perfil_form.is_valid():
            user = form.save(commit=False)
            perfil = perfil_form.save(commit=False)
            user.password = make_password(user.password)
            user.save()
            perfil.user = user
            perfil.nome = user.first_name+' '+user.last_name
            perfil.save()
            user_login(request)
            return redirect('/')
    else:
        form = UserForm()
        perfil_form = PerfilForm()

    return render(request, 'auth/signup.html', {'form': form, 'perfil_form':perfil_form})
