from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib import messages

def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    else :
        firstname = request.POST.get('nome')
        lastname = request.POST.get('sobrenome')
        cep = request.POST.get('cep')
        email = request.POST.get('email')
        password = request.POST.get('password')

        getUsersDb = User.objects.get(email=email)
        if getUsersDb:
            messages.info(request, "Email already registered")

        messages.info(request, firstname)
        return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')

def index(request):
    return render(request, 'index.html')

#@login_required
def logout(request):
    #logout_django(request)
    return render(request, 'login.html')