from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from core.models import User


def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    else:
        firstname = request.POST.get('nome')
        lastname = request.POST.get('sobrenome')
        cpf = request.POST.get('cpf')
        cep = request.POST.get('cep')
        address_number = request.POST.get('numero')
        email = request.POST.get('email')
        password = request.POST.get('password')

        email_exists = User.objects.filter(email=email).exists()
        if email_exists:
            messages.error(request, "Email já está cadastrado!")
            return render(request, 'register.html')
        else:
            User.objects.create_user(username=email, email=email, password=password,
                                     first_name=firstname, last_name=lastname, cpf=cpf,
                                     cep=cep, address_number=address_number)
            messages.info(request, "Cadastrado com sucesso, agora só fazer o login ;-)")
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
            return redirect('index')
        else:
            messages.error(request, 'Email ou senha inválidos!')
            return render(request, 'login.html')


@login_required
def index(request):
    if request.user.is_authenticated:
        messages.info(request, 'Bem vindo!')
        return render(request, 'index.html')
    return redirect('login')

@login_required
def logout(request):
    logout(request)
    return render(request, 'login.html')