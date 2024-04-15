from django.urls import path
from .views import index, perfil, registro, cerrarSesion, inicioSesion, categorias,productos, carrito, detalle, interior, exterior, suculentas, carnivoras, huerto, insumos, eliminar

urlpatterns = [
        path('', index),
        path('perfil/', perfil),
        path('registro/', registro),
        path('categorias/', categorias, name='categorias'),
        path('productos/<int:id>/', productos, name="productos"),
        path('detalle/<int:id>/', detalle, name="detalle"),
        path('detalle/', detalle, name='detalle'), 
        path('productos/interior/', interior),
        path('productos/exterior/', exterior),
        path('productos/suculentas/', suculentas),
        path('productos/carnivoras/', carnivoras),
        path('productos/huerto/', huerto),
        path('productos/insumos/', insumos),
        path('carrito/', carrito, name='carrito'),
        path('eliminar/<int:id>/', eliminar, name="eliminar"),
        path('inicioSesion/', inicioSesion),
        path('cerrarSesion/', cerrarSesion),
        
]