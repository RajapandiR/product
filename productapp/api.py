from rest_framework import viewsets, status
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

class ProfileApiView(APIView):
	serializer_class = serializers.ProfileSerializer
	def get(self, request,  format = None):
		obj = models.Profile.objects.all()
		serializer = serializers.ProfileSerializer(obj, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = self.serializer_class(data=request.data)
		if serializer.is_valid():
			serializer.save()
			message = f'Create Successfull'
			return Response({'message':message})
		else:
			return Response(
				serializer.errors,
				status = status.HTTP_400_BAD_REQUEST
				)	
class CategoryApiView(APIView):
	serializer_class = serializers.CategorySerializer
	def get(self, request,  format = None):
		obj = models.Category.objects.all()
		serializer = serializers.CategorySerializer(obj, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = self.serializer_class(data=request.data)
		if serializer.is_valid():
			serializer.save()
			message = f'Create Successfull'
			return Response({'message':message})
		else:
			return Response(
				serializer.errors,
				status = status.HTTP_400_BAD_REQUEST
				)	

class ProductApiView(APIView):
	serializer_class = serializers.ProductSerializer
	def get(self, request,  format = None):
		obj = models.Product.objects.all()
		serializer = serializers.ProductSerializer(obj, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = self.serializer_class(data=request.data)
		if serializer.is_valid():
			serializer.save()
			message = f'Create Successfull'
			return Response({'message':message})
		else:
			return Response(
				serializer.errors,
				status = status.HTTP_400_BAD_REQUEST
				)

class OrderApiView(APIView):
	serializer_class = serializers.OrderSerializer
	def get(self, request,  format = None):
		obj = models.Order.objects.all()
		serializer = serializers.OrderSerializer(obj, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = self.serializer_class(data=request.data)
		if serializer.is_valid():
			serializer.save()
			message = f'Create Successfull'
			return Response({'message':message})
		else:
			return Response(
				serializer.errors,
				status = status.HTTP_400_BAD_REQUEST
				)	

class InvoiceApiView(APIView):
	serializer_class = serializers.InvoiceSerializer
	def get(self, request,  format = None):
		obj = models.Invoice.objects.all()
		serializer = serializers.InvoiceSerializer(obj, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = self.serializer_class(data=request.data)
		if serializer.is_valid():
			serializer.save()
			message = f'Create Successfull'
			return Response({'message':message})
		else:
			return Response(
				serializer.errors,
				status = status.HTTP_400_BAD_REQUEST
				)	