from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from orders.endpoints import *

router = DefaultRouter()
router.register(r'orders', OrdersAPI)
router.register(r'shops', ShopAPI, basename='shop')
router.register(r'posts', PostAPI)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('orders/', include('orders.urls')),
    path('news/', include('news.urls')),
    path('api/v1/', include(router.urls))
]
