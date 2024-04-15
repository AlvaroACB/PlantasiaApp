from django.urls import path
from .views import index, perfil, registro, cerrarSesion, inicioSesion, categorias,productos, modificarPerfil, carrito, detalle, eliminar, recuperar

urlpatterns = [
        path('', index),
        path('perfil/', perfil),
        path('registro/', registro),
        path('categorias/', categorias, name='categorias'),
        path('productos/<int:id>/', productos, name="productos"),
        path('detalle/<int:id>/', detalle, name="detalle"),
        path('detalle/', detalle, name='detalle'), 

        path('carrito/', carrito, name='carrito'),
        path('eliminar/<int:id>/', eliminar, name="eliminar"),
        path('inicioSesion/', inicioSesion),
        path('cerrarSesion/', cerrarSesion),
        path('modificarPerfil/', modificarPerfil, name="modificarPerfil"),
        path('recuperar/', recuperar),

]