from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect


# Create your views here.


def index(request):
    return render(request, "index.html")


def home(request):
    return render(request, "home.html")


def purchase(request):
    if request.method == 'POST':
        messages.success(request, 'Order Placed Successfully!')
        return HttpResponseRedirect(request.path)
    return render(request, "purchase.html")


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Invalid Username or Password!")
            return redirect('login')
    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already taken!")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, "Password not matched!")
            return redirect('register')
        return redirect('/')
    return render(request, "register.html")


def logout(request):
    auth.logout(request)
    return redirect('login')


