from django.urls import path
from .views import index, perfil, registro, cerrarSesion, inicioSesion, categorias,productos , interior, exterior, suculentas, carnivoras, huerto, insumos

urlpatterns = [
        path('', index),
        path('perfil/', perfil),
        path('registro/', registro),
        path('categorias/', categorias, name='categorias'),
        path('productos/<int:id>/', productos, name="productos"),
        path('productos/interior/', interior),
        path('productos/exterior/', exterior),
        path('productos/suculentas/', suculentas),
        path('productos/carnivoras/', carnivoras),
        path('productos/huerto/', huerto),
        path('productos/insumos/', insumos),
        path('inicioSesion/', inicioSesion),
        path('cerrarSesion/', cerrarSesion),
        
]