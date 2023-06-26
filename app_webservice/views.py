from django.shortcuts import render
from django.http import JsonResponse
from .models import Product

from rest_framework import serializers, viewsets, permissions
from .models import Stock, Movement, User
from .serializers import ProductSerializer, StockSerializer, MovementSerializer, UserSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status





print('hola mundo, soy el archivo views.py')





class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # renderer_classes = (JSONRenderer, )
    # authentication_classes = (SessionAuthentication)
    # permission_classes = (permissions.AllowAny, )


class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    # renderer_classes = (JSONRenderer, )
    # authentication_classes = (SessionAuthentication)
    # permission_classes = (permissions.AllowAny,) #IsAdminUser, IsAuthenticated, )


class MovementViewSet(viewsets.ModelViewSet):
    queryset = Movement.objects.all()
    serializer_class = MovementSerializer
    # renderer_classes = (JSONRenderer, )
    # authentication_classes = (SessionAuthentication,)
    # permission_classes = (permissions.AllowAny,) #IsAdminUser, IsAuthenticatedOrReadOnly, )










@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def product_detail(request, product_code):
    try:
        product = Product.objects.get(code=product_code)
    except Product.DoesNotExist:
        return Response({'error': f'Product with code {product_code} does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    elif request.method in ('PUT', 'PATCH'):
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()

            # Actualizar la cantidad de stock si se proporciona en los datos de la solicitud
            stock_quantity = request.data.get('stock_quantity')
            if stock_quantity is not None:
                product.stock.quantity = stock_quantity
                product.stock.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    return Response({'error': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)








@api_view(['POST', 'PUT', 'PATCH', 'DELETE'])
def manage_stock(request, product_code):
    try:
        product = Product.objects.get(code=product_code)
    except Product.DoesNotExist:
        return Response({'error': f'Product with code {product_code} does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        quantity = request.data.get('quantity')
        stock = Stock.objects.create(product=product, quantity=quantity)
        serializer = StockSerializer(stock)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    elif request.method in ('PUT', 'PATCH'):
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True, 'quantity': product.stock.quantity})
        else:
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            stock = Stock.objects.get(product=product)
            stock.delete()
        except Stock.DoesNotExist:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)


    return Response({'error': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)








