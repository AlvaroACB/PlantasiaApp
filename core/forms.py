from django.forms import ModelForm
from django.contrib.auth.models import User

class FormRegistro(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

class FormInicioSesion(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']