from django.urls import path
from .views import index, apiPlantas, perfil, registro, cerrarSesion, inicioSesion, inventario, categorias,productos, modificarInventario, eliminarInventario ,modificarPerfil, carrito, detalle, eliminar, recuperar

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
        path('inventario/', inventario, name='inventario'),
        path('modificarInventario/<int:id>', modificarInventario, name='modificarInventario'),
        path('eliminarInventario/<int:id>', eliminarInventario, name='eliminarInventario'),
        path('proximamente/', apiPlantas),
]