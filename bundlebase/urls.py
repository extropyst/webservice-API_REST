"""
URL configuration for bundlebase project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from app_webservice import api
from app_webservice.views import ProductViewSet, StockViewSet
from app_webservice import views
from rest_framework.documentation import include_docs_urls

print('hola mundo, soy el archivo urls.py (bundlebase)')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_webservice.urls')),
    path('docs/', include_docs_urls(title='Api Documentation')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



    # path('./product/<str:product_code>/delete_product/', views.delete_product),
    # path('./product/<str:product_code>/update_stock/', views.update_stock),
    # path('./product/<str:product_code>/update_stock_patch/', views.update_stock_patch),
    # path('./stock/add_stock/', views.add_stock),
    # path('./stock/<str:product_code>/delete_stock/', views.delete_stock),
