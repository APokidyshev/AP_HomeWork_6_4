from rest_framework import serializers
from models import Product, Review


class ReviewSerializer(serializers.ModelSerializer):
    # реализуйте все поля
    class Meta:
        model = Review
        fields = ['product', 'text', 'mark', 'created_at']
    # pass


class ProductListSerializer(serializers.Serializer):
    # реализуйте поля title и price
    title = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    # pass


class ProductDetailsSerializer(serializers.ModelSerializer):
    # реализуйте поля title, description, price и reviews (список отзывов к товару)
    pass
