
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    class Meta:
        model = Product
        fields = ['id', 'name','image']
