from rest_framework import viewsets
from rest_framework.views import APIView, Response

from productapp import serializers
from productapp import models

class ProfileViewSet(viewsets.ModelViewSet):
	serializer_class = serializers.ProfileSerializer
	queryset = models.Profile.objects.all()

class CategoryViewSet(viewsets.ModelViewSet):
	serializer_class = serializers.CategorySerializer
	queryset = models.Category.objects.all()

class ProductViewSet(viewsets.ModelViewSet):
	serializer_class = serializers.ProductSerializer
	queryset = models.Product.objects.all()

# class ProductApiView(APIView):
# 	serializer_class = serializers.ProductSerializer
# 	def get(self, request,  format = None):
# 		obj = models.Product.objects.all()
# 		serializer = serializers.ProductSerializer(obj, many=True)
# 		return Response(serializer.data)
class CategoryApiView(APIView):
	serializer_class = serializers.CategorySerializer
	def get(self, request,  format = None):
		obj = models.Category.objects.all()
		serializer = serializers.CategorySerializer(obj, many=True)
		return Response(serializer.data)


class ProductApiView(APIView):
	serializer_class = serializers.ProductSerializer
	def get(self, request,  format = None):
		obj = models.Product.objects.all()
		serializer = serializers.ProductSerializer(obj, many=True)
		return Response(serializer.data)