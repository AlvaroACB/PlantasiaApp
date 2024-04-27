from rest_framework import serializers
from core.models import Categoria, Producto

class CategoriaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['categoria_id', 'nombre_categ', 'img_categ']
        
class ProductoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['producto_id', 'nombre_prod', 'descripcion_prod', 'valor_prod','categoria', 'img_prod']
          