from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=settings.ROLES)

    def __str__(self):
        return self.user.username + ' - ' + self.role
    
class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_categoria

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=50)
    desc_producto = models.CharField(max_length=100)
    precio = models.PositiveIntegerField(default=0)
    id_categoria = models.ForeignKey("Categoria", on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_producto