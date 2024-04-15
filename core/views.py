from django.shortcuts import render, redirect
from .forms import FormRegistro, FormInicioSesion, FormCarrito, FormModificarUsuario
from .models import UserProfile, Categoria, Producto, Carrito
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
                profile = UserProfile.objects.create(user=user, role = 'Cliente')
                profile.save()
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
        usuario = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if usuario is None:
            return render(request, 'inicioSesion.html', datosErr)
        else:
            profile = UserProfile.objects.get(user=usuario)
            request.session['perfil'] = profile.role
            login(request, usuario)
            return redirect('/perfil')
    return render(request, 'inicioSesion.html', datos)

def cerrarSesion(request):
    logout(request)
    return redirect('/')

def categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias.html', {'categorias': categorias})

def productos(request, id):
    productos = Producto.objects.filter(categoria_id = id)
    categoria = Categoria.objects.get(pk = id)
    return render(request, 'productos.html', {'productos': productos, 'categoria': categoria})

def detalle(request, id):
    productos = Producto.objects.get(producto_id = id)
    if request.method == 'POST':
        formulario = FormCarrito(request.POST) 
        formulario.save()     
    return render(request, 'detalle.html', {'productos': productos})

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

@login_required
def carrito(request):
    usuario = request.user.id
    items = Carrito.objects.filter(usuario=usuario)
    datos = {
        'items': items
    }
    return render(request, 'carrito.html', datos)

def eliminar(request, id):
    item = Carrito.objects.get(id=id)
    item.delete()
    return redirect('/carrito')


def modificarPerfil(request):
    usuario = User.objects.get(id=request.user.id)
    if request.method == 'POST':
        formulario = FormModificarUsuario(data=request.POST, instance=usuario)
        if formulario.is_valid():
            formulario.save()
            print("listooo")
            return redirect('/perfil')
    return render(request, 'modificarPerfil.html')