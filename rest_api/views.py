from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status

from core.models import Categoria, Producto
from .serializers import CategoriaSerializers, ProductoSerializers
#librerias de aunteticacion
from rest_framework.decorators import permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))
def lista_categoria(request):
    if request.method == 'GET':
        categoria = Categoria.objects.all()
        serializer = CategoriaSerializers(categoria,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CategoriaSerializers(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            print('error', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','PATCH','DELETE'])
@permission_classes((IsAuthenticated,))
def vista_categoria(request, id):
	try:
		categoria = Categoria.objects.get(pk=id)
	except categoria.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
	if request.method == 'GET':
		serializer = CategoriaSerializers(categoria)
		return Response(serializer.data)
	elif request.method == 'PUT' or request.method == 'PATCH':
		data = JSONParser().parse(request)
		serializer = CategoriaSerializers(categoria,data=data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
	elif request.method == 'DELETE':
		categoria.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)    

#problema con producto.stock
@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))
def lista_productos(request):
    if request.method == 'GET':
        producto = Producto.objects.all()
        serializer = ProductoSerializers(producto,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductoSerializers(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            print('error', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#problema con producto.stock       
@api_view(['GET','PUT','PATCH','DELETE'])
@permission_classes((IsAuthenticated,))
def vista_produtos(request, id):
	try:
		producto = Categoria.objects.get(pk=id)
	except producto.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
	if request.method == 'GET':
		serializer = ProductoSerializers(producto)
		return Response(serializer.data)
	elif request.method == 'PUT' or request.method == 'PATCH':
		data = JSONParser().parse(request)
		serializer = ProductoSerializers(producto,data=data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
	elif request.method == 'DELETE':
		producto.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)   