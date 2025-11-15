from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Producto
from .serializers import ProductoSerializer

# Vista para listar y crear productos
class ProductoListCreate(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

# Vista para actualizar y eliminar un producto
class ProductoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
