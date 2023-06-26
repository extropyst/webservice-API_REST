from rest_framework import routers
from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from app_webservice import views
from app_webservice.views import ProductViewSet, StockViewSet



print('hola mundo, soy el archivo urls.py (app_webservice)')


router = routers.DefaultRouter()

router.register(r'product', ProductViewSet, 'product')

router.register(r'stock', StockViewSet, 'stock')


urlpatterns = router.urls

