from django.urls import path
from .views import *

urlpatterns = [
    path('all/', all_orders, name='all-orders-page'),
    path('my/', my_orders, name='my-orders-page'),
    path('new/', add_new, name='add-new-order')
]
