from rest_framework import serializers
from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['codigo', 'descripcion', 'precio', 'tipo']
    
    def validate_precio(self, value):
        if not isinstance(value, (int, float)):  # Asegúrate de que el precio sea un número
            raise serializers.ValidationError("El precio debe ser un número.")
        if value < 100:
            raise serializers.ValidationError("El precio debe ser al menos 100.")
        return value
