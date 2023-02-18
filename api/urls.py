from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import *

router = SimpleRouter()
router.register(r'statuses', CardStatusViewSet)
router.register(r'series', CardSeriesViewSet)
router.register(r'cards', CardViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'orderProducts', OrderProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', expired_obtain_auth_token)
]
