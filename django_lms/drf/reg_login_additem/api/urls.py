from django.urls import path, include

from rest_framework import routers
from .views import CategoryViewSet, ItemViewSet, RegisterAPI

router = routers.DefaultRouter()
router.register(r'category_product', CategoryViewSet)
router.register(r'product_item', ItemViewSet)


urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/', include(router.urls)),
]
