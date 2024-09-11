from django.db.models import F
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import *


class OrdersAPI(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = GetOrderSerializer
    permission_classes = [permissions.AllowAny]

    @action(methods=['get'], detail=False)
    def all(self, request):
        queryset = Orders.objects.all().annotate(address=F('shop__address'),
                                                 district=F('shop__district__name'),
                                                 city=F('shop__district__city__name'),
                                                 post_name=F('post__name'))
        return Response(GetOrderSerializer(queryset, many=True).data)

    @action(methods=['get'], detail=False)
    def my(self, request):
        queryset = Orders.objects.filter(author=request.user.id).annotate(address=F('shop__address'),
                                                                          district=F('shop__district__name'),
                                                                          city=F('shop__district__city__name'),
                                                                          post_name=F('post__name'))
        return Response(GetOrderSerializer(queryset, many=True).data)

    @action(methods=['delete'], detail=True)
    def delete_my(self, request, pk=None):
        order = get_object_or_404(Orders, pk=pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserOrdersAPI(viewsets.ModelViewSet):
    serializer_class = GetOrderSerializer

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        if not user_id:
            return None
        return Orders.objects.filter(user=user_id).annotate(address=F('shop__address'),
                                                            district=F('shop__district__name'),
                                                            city=F('shop__district__city__name'),
                                                            post_name=F('post__name'))


class ShopAPI(viewsets.ModelViewSet):
    queryset = Shop.objects.all()

    @action(methods=['get'], detail=False)
    def all(self, request):
        queryset = Shop.objects.all()
        return Response(ShopSerializer(queryset, many=True).data)

    @action(methods=['get'], detail=False)
    def my(self, request):
        queryset = Shop.objects.filter(director=request.user.id)
        return Response(ShopSerializer(queryset, many=True).data)


class PostAPI(viewsets.ModelViewSet):
    queryset = apps.get_model('accounts', 'Post').objects.all()
    serializer_class = PostSerializer
    http_method_names = ['get']
