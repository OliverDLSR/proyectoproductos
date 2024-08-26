from rest_framework import generics
from .models import Producto
from .serializers import ProductoSerializer
from django.shortcuts import render

class ProductoListCreateView(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


def index(request):
    return render(request, 'index.html')
