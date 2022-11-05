from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from account.forms import UserForm


def user_login(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, 'result.html', {'result': "Success"})
        else:
            return render(request, 'result.html', {'result': "Failed"})
    return render(request, 'auth/login.html')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def user_signup(request):
    if request.method =='POST':
        form = UserForm(request.POST)
        if form.is_valid():
            print(form.save())
    else:
        form = UserForm()

    return render(request,'auth/signup.html',{'form':form})
