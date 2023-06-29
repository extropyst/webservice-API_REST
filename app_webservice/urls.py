from rest_framework import routers
from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from app_webservice import views
from app_webservice.views import ProductViewSet, StockViewSet, MovementViewSet, UserViewSet



print('hola mundo, soy el archivo urls.py (app_webservice)')


router = routers.DefaultRouter()

router.register(r'product', ProductViewSet, 'product')

router.register(r'stock', StockViewSet, 'stock')

router.register(r'movimientos', MovementViewSet, 'movement')

router.register(r'users', UserViewSet, 'user')

urlpatterns = router.urls

