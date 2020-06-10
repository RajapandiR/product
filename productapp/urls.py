from django.urls import path, include

from productapp import api

urlpatterns = [
	path('product/', api.ProductApiView.as_view()),
	path('category/', api.CategoryApiView.as_view()),
	path('profile/', api.ProfileApiView.as_view()),
	path('order/', api.OrderApiView.as_view()),
]