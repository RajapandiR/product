from django.urls import path, include
from rest_framework import routers

from productapp import api

router = routers.DefaultRouter()
router.register('profile', api.ProfileViewSet)
router.register('category', api.CategoryViewSet)

urlpatterns = [
	path('api/', include(router.urls))
]