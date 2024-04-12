from django.urls import path
from .views import index, perfil, registro, cerrarSesion, inicioSesion, categorias, interior, exterior, suculentas, carnivoras, huerto, insumos

urlpatterns = [
        path('', index),
        path('perfil/', perfil),
        path('registro/', registro),
        path('categorias/', categorias),
        path('productos/interior/', interior),
        path('productos/exterior/', exterior),
        path('productos/suculentas/', suculentas),
        path('productos/carnivoras/', carnivoras),
        path('productos/huerto/', huerto),
        path('productos/insumos/', insumos),
        path('inicioSesion/', inicioSesion),
        path('cerrarSesion/', cerrarSesion),
        
]