from django.urls import path
from .views import index, perfil, registro, cerrarSesion, inicioSesion

urlpatterns = [
        path('', index),
        path('perfil/', perfil),
        path('registro/', registro),
        path('inicioSesion/', inicioSesion),
        path('cerrarSesion/', cerrarSesion),
]