from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from account.forms import UserForm, UserLoginForm
from account.models import User


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
            return render(request, 'result.html', {'result': "Success"})
        else:
            return render(request, 'result.html', {'result': "Failed"})
    else:
        form = UserLoginForm()
    return render(request, 'auth/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def user_signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = UserForm(request.POST)
        print(form)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.password = make_password(new_user.password)
            new_user.save()
            user_login(request)
            return redirect('/')
    else:
        form = UserForm()

    return render(request, 'auth/signup.html', {'form': form})
