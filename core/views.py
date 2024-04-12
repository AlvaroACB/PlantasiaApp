from django.shortcuts import render, redirect
from .forms import FormRegistro, FormInicioSesion
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError


def index(request):
    return render(request, 'index.html')

@login_required
def perfil(request):
    return render(request, 'perfil.html')

def registro(request):
    datos = {
        'form': FormRegistro()
    }
    datosErr = {
        'form': FormRegistro(),
        'error': "Las contraseñas no coinciden"
    }
    if request.method == 'GET':
            return render(request, 'registro.html', datos)
    else:
        if request.POST["password"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(username=request.POST["username"],
                                                first_name=request.POST["first_name"],
                                                last_name=request.POST["last_name"],
                                                email=request.POST["email"],
                                                password=request.POST["password"],
                                                )
                user.save()
                username1 = request.POST["username"]
                password1 = request.POST["password"]
                usuario1 = authenticate(request, username=username1, password=password1)
                login(request, usuario1)
                return redirect('/perfil')
            except IntegrityError:
                return render(request, 'registro.html', datos)
        else:
            return render(request, 'registro.html', datosErr)

def inicioSesion(request):
    datos = {
        'form': FormInicioSesion()
    }
    datosErr = {
        'form': FormInicioSesion(),
        'error': "Usuario o contraseña incorrectos."
    }
    if request.method == 'POST':
    #1
        usuario = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if usuario is None:
            return render(request, 'inicioSesion.html', datosErr)
        else:
	  #2    
            profile = UserProfile.objects.get(user=usuario)
            request.session['perfil'] = profile.role
            login(request, usuario)
            return redirect('/perfil')
    return render(request, 'inicioSesion.html', datos)

def cerrarSesion(request):
    logout(request)
    return redirect('/')

def categorias(request):
    return render(request, 'categorias.html')

def interior(request):
    return render(request, 'productos/interior.html')

def exterior(request):
    return render(request, 'productos/exterior.html')

def suculentas(request):
    return render(request, 'productos/suculentas.html')

def carnivoras(request):
    return render(request, 'productos/carnivoras.html')

def huerto(request):
    return render(request, 'productos/huerto.html')

def insumos(request):
    return render(request, 'productos/insumos.html')