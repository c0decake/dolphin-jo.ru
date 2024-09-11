from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import RegisterUser


def login_user(request):
    if request.method == 'POST':
        user = authenticate(request,
                            username=request.POST.get('login'),
                            password=request.POST.get('password'))
        if user:
            login(request, user)
            return redirect(to='news-page')
    return render(request, 'accounts/login.html')


def logout_user(request):
    logout(request)
    return redirect(to='login-page')


def register_user(request):
    if request.method == 'POST':
        form = RegisterUser(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            return redirect(to='login-page')
    return render(request, 'accounts/register.html')


def profile(request):
    return HttpResponse("fdsfsd")
