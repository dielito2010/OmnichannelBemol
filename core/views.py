from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from core.models import User


def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    else:
        firstname = request.POST.get('nome')
        lastname = request.POST.get('sobrenome')
        cep = request.POST.get('cep')
        email = request.POST.get('email')
        password = request.POST.get('password')

        email_exists = User.objects.filter(email=email).exists()
        if email_exists:
            messages.info(request, "Email already registered")
            return render(request, 'register.html')
        else:
            User.objects.create_user(username=email, email=email, password=password, first_name=firstname, last_name=lastname, cep=cep)
            messages.info(request, "User registered successfully")
            return redirect('login')


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)
        if user:
            auth_login(request, user)
            return redirect('index')  # Mensagens serão redirecionadas automaticamente
        else:
            messages.error(request, 'Invalid user or password')
            return render(request, 'login.html')


@login_required
def index(request):
    if request.user.is_authenticated:
        messages.info(request, 'Successfully, wellcome!')
        return render(request, 'index.html')
    return redirect('login')

@login_required
def logout(request):
    logout(request)
    return render(request, 'login.html')