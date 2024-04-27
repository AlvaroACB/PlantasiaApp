from django.urls import path
from . import views

urlpatterns = [
        path('categorias/', views.lista_categoria, name="lista_categorias"),
        path('categorias/<id>', views.vista_categoria, name='vista_categorias'),
        path('productos/', views.lista_productos, name="lista_productos"),
        path('productos/<id>', views.vista_productos, name='vista_productos'),
]