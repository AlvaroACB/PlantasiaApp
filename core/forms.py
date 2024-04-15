from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Producto, Carrito

class FormRegistro(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

class FormInicioSesion(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class FormModificarUsuario(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class FormCarrito(ModelForm):
    class Meta:
        model = Carrito
        fields = ['nombre_prod', 'valor_prod', 'cantidad_prod', 'producto', 'usuario']

class FormRecuperar(ModelForm):
    class Meta:
        model = User
        fields = ['email']