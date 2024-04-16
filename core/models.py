from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=settings.ROLES)

    def __str__(self):
        return self.user.username + ' - ' + self.role
    
class Categoria(models.Model):
    categoria_id = models.IntegerField(primary_key=True)
    nombre_categ = models.CharField(max_length=25)
    img_categ = models.ImageField(upload_to="categorias", null=True)
    
    def __str__(self):
        return self.nombre_categ

    class Meta:
        managed = False
        db_table = 'categoria'

class Compra(models.Model):
    compra_id = models.IntegerField(primary_key=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    estado_compra = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'compra'

class Producto(models.Model):
    producto_id = models.IntegerField(primary_key=True)
    nombre_prod = models.CharField(max_length=25)
    descripcion_prod = models.CharField(max_length=300)
    valor_prod = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    stock = models.IntegerField()
    img_prod = models.ImageField(upload_to="productos", null=True)

    def __str__(self):
        return self.nombre_prod

    class Meta:
        managed = False
        db_table = 'producto'
        
class DetalleCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'detalle_compra'
        
class Carrito(models.Model):
    nombre_prod = models.CharField(max_length=25)
    valor_prod = models.IntegerField()
    cantidad_prod = models.IntegerField()
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)