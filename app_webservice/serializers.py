from rest_framework import serializers
from .models import Product, Stock, Movement, User








# class StockField(serializers.IntegerField):
#     def to_representation(self, value):
#         return value

#     def to_internal_value(self, data):
#         try:
#             return int(data)
#         except (TypeError, ValueError):
#             raise serializers.ValidationError('Invalid value')




class ProductSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField()
    stock = serializers.IntegerField(read_only=True)
    # stock_quantity = serializers.IntegerField(read_only=True)
    stock_add = serializers.IntegerField(required=False, min_value=0, write_only=True)
    image_upload = serializers.ImageField(write_only=True)


    def create(self, validated_data):
        image = validated_data.pop('image_upload', None)
        stock_data = validated_data.pop('stock_add', None)
        if stock_data:
            # stock_quantity = Stock['quantity']
            stock_quantity = Stock.objects.create(quantity=stock_data)
            validated_data['stock_add'] = stock_quantity.id
        instance = super().create(validated_data)


        if stock_quantity:
            instance.stock = stock_quantity
            instance.save()

        if image:
            instance.photo = image
            instance.save()
        return instance

    def update(self, instance, validated_data):
        stock_data = validated_data.pop('stock_update', None)
        if stock_data is not None:
            instance.stock.quantity = stock_data
            instance.stock.save()

        if 'image_upload' in validated_data:
            instance.photo = validated_data.pop('image_upload')
        return super().update(instance, validated_data)

    def get_photo(self, product):
        request = self.context.get('request')
        if product.photo:
            return request.build_absolute_uri(product.photo.url)
        else:
            return None

    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['created_at', ]

    # def to_representation(self, instance):
    #     ret = super().to_representation(instance)
    #     if hasattr(instance, 'stock_quantity'):
    #         ret['stock_quantity'] = instance.stock_quantity
    #     return ret











class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'
        # read_only_fields = ['created_at',]




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        # read_only_fields = ['created_at', 'updated_at',]



class MovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movement
        fields = '__all__'
        # read_only_fields = ['created_at', 'updated_at',]