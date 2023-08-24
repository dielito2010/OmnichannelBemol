from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
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
            # Aqui você pode criar o usuário usando o modelo personalizado de usuário
            user = User.objects.create_user(username=email, email=email, password=password, first_name=firstname, last_name=lastname, cep=cep)
            messages.info(request, "User registered successfully")
            return redirect('login') 


def login(request):
    return render(request, 'login.html')

def index(request):
    return render(request, 'index.html')

#@login_required
def logout(request):
    #logout_django(request)
    return render(request, 'login.html')