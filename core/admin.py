from django.contrib import admin
from .models import UserProfile, Categoria, Producto

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Categoria)
admin.site.register(Producto)