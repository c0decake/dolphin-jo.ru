from django.urls import path
from .views import *

urlpatterns = [
    path('', news_page, name='news-page'),
]
