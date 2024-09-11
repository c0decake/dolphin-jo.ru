from django.apps import apps
from rest_framework import serializers

from .models import Orders, Shop


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'


class GetOrderSerializer(OrderSerializer):
    address = serializers.CharField(read_only=True)
    district = serializers.CharField(read_only=True)
    city = serializers.CharField(read_only=True)
    post_name = serializers.CharField(read_only=True)

    class Meta:
        model = Orders
        fields = [
            'id',
            'author',
            'rating',
            'work_date',
            'time_in',
            'time_out',
            'price',
            'taxi_to',
            'taxi_from',
            'food',
            'drinks',
            'toilet',
            'address',
            'district',
            'city',
            'post_name'
        ]


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model('accounts', 'Post')
        fields = '__all__'
