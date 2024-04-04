import json
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from serializers import ReviewSerializer, ProductListSerializer, ProductDetailsSerializer
from models import Product, Review

@api_view(['GET'])
def products_list_view(request):
    # """реализуйте получение всех товаров из БД
    # реализуйте сериализацию полученных данных
    # отдайте отсериализованные данные в Response"""
    ser = ProductListSerializer(Product.objects.all(), many=True)
    return Response(ser.data)
    # pass


class ProductDetailsView(APIView):
    def get(self, request, product_id):
        # """реализуйте получение товара по id, если его нет, то выдайте 404
        # реализуйте сериализацию полученных данных
        # отдайте отсериализованные данные в Response"""
        pass


# доп задание:
class ProductFilteredReviews(APIView):
    def get(self, request, product_id):
        # """обработайте значение параметра mark и
        # реализуйте получение отзывов по конкретному товару с определённой оценкой
        # реализуйте сериализацию полученных данных
        # отдайте отсериализованные данные в Response"""
        pass
