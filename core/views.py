from django.shortcuts import render, redirect
from .forms import FormRegistro, FormInicioSesion, FormCarrito, FormModificarUsuario, FormRecuperar, FormModInv
from .models import UserProfile, Categoria, Producto, Carrito
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from .decorators import role_required


def index(request):
    perfil = request.session.get('perfil')
    context = {
        'perfil':perfil,
    }
    return render(request, 'index.html', context)

@login_required
def perfil(request):
    perfil = request.session.get('perfil')
    context = {
        'perfil':perfil,
    }
    return render(request, 'perfil.html', context)

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
    perfil = request.session.get('perfil')
    categorias = Categoria.objects.all()
    context = {
        'categorias': categorias,
        'perfil':perfil,
    }
    return render(request, 'categorias.html', context)

def productos(request, id):
    productos = Producto.objects.filter(categoria_id = id)
    categoria = Categoria.objects.get(pk = id)
    perfil = request.session.get('perfil')
    context = {
        'perfil':perfil,
        'productos': productos,
        'categoria': categoria
    }
    return render(request, 'productos.html', context)

def detalle(request, id):
    productos = Producto.objects.get(producto_id = id)
    perfil = request.session.get('perfil')
    context = {
        'perfil':perfil,
        'productos':productos
    }
    hay_producto_en_carro = Carrito.objects.filter(producto = id)
    if request.method == 'POST':
        formulario = FormCarrito(request.POST)
        if formulario.is_valid():
            if not hay_producto_en_carro.exists():
                formulario.save()
            else:
                cantidad_agregada = formulario.cleaned_data.get('cantidad_prod')
                print(cantidad_agregada)
                cantidad_nueva = 0
                for item in hay_producto_en_carro:
                    cantidad_nueva = cantidad_agregada + item.cantidad_prod
                print(cantidad_nueva)
                Carrito.objects.filter(producto = id).update(cantidad_prod= cantidad_nueva)
           
    return render(request, 'detalle.html', context)

@login_required
def carrito(request):
    usuario = request.user.id
    items = Carrito.objects.filter(usuario=usuario)
    perfil = request.session.get('perfil')
    context = {
        'perfil':perfil,
        'items':items,
    }
    return render(request, 'carrito.html', context)

def eliminar(request, id):
    item = Carrito.objects.get(id=id)
    item.delete()
    return redirect('/carrito')

@login_required
def modificarPerfil(request):
    usuario = User.objects.get(id=request.user.id)
    perfil = request.session.get('perfil')
    context = {
        'perfil':perfil,
    }
    if request.method == 'POST':
        formulario = FormModificarUsuario(data=request.POST, instance=usuario)
        if formulario.is_valid():
            formulario.save()
            print("listooo")
            return redirect('/perfil')
    return render(request, 'modificarPerfil.html', context)

def recuperar(request):
    perfil = request.session.get('perfil')
    datos = {
        'form': FormRecuperar()
    }
    datosErr = {
        'form': FormRecuperar(),
        'error': "Correo inexistente.",
    }
    if request.method == 'POST':
        email = request.POST['email']
        try:
            email_recuperar = User.objects.get(email=email)
            x=email_recuperar.email
        except ObjectDoesNotExist:
            return render(request, 'recuperar.html', datosErr)
        if email ==  x:
            datos = {
            'form': FormRecuperar(),
            'error': "Su contraseña fue enviada a su correo"
            }
            return render(request, 'recuperar.html', datos)
        else:
            return render(request, 'recuperar.html', datosErr)
    return render(request, 'recuperar.html', datos)

@role_required('admin')
def inventario(request):
    perfil = request.session.get('perfil')
    productos = Producto.objects.all()
    datos = {
        'productos': productos, 'perfil':perfil,
    }
    return render(request, 'inventario.html', datos)

@role_required('admin')
def modificarInventario(request, id):
    perfil = request.session.get('perfil')
    producto = Producto.objects.get(producto_id=id) 
    datos = { 'producto': producto, 'perfil':perfil, }
    if request.method == 'POST':
        formulario = FormModInv(data=request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
    return render(request, 'modificarInventario.html', datos)

@role_required('admin')
def eliminarInventario(request, id):
    producto = Producto.objects.get(producto_id=id)
    producto.delete()
    return redirect("/inventario")