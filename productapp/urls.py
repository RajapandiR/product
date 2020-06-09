from django.urls import path, include
from rest_framework import routers

from productapp import api

router = routers.DefaultRouter()
router.register('profile', api.ProfileViewSet)
router.register('category', api.CategoryViewSet)
# router.register('product', api.ProductViewSet)
# router.register('product', api.ProductApiView.as_view())

urlpatterns = [
	path('api/', include(router.urls)),
	path('product/', api.ProductApiView.as_view()),
	path('category/', api.CategoryApiView.as_view()),
]