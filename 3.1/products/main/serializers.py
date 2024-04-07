from rest_framework import serializers
from main.models import Product, Review


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
    reviwes = ReviewSerializer(many=True, read_only=True)

    # реализуйте поля title, description, price и reviews (список отзывов к товару)
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price',  'reviwes']
    # pass
