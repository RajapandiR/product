from rest_framework import viewsets

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