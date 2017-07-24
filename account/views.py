from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as _login, logout as _logout
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            _login(request, user)
            return redirect("/")
        else:
            messages.add_message(request, messages.INFO, '로그인 실패')
    return render(request, 'account/login.html')

def logout(request):
    _logout(request)
    return redirect("/")

def index(request):
    return render(request, 'account/login.html')

def signup(request):
    return render(request, 'account/signup.html')

def useradd(request):
    username = request.POST['username']
    password = request.POST['password']
    name = request.POST['name']
    email = request.POST['email']
    phone_number = request.POST['phone_number']
    area = request.POST['area']
    print(area)
    useradd = User(username=username, password=password,
                   name=name, email=email, phone_number=phone_number)
    useradd.set_password(password)
    useradd.area = area
    print(useradd.area)
    useradd.save()
    print(useradd.area)
    return HttpResponseRedirect("/account/login/")


