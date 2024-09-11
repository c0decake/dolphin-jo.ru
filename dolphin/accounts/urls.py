from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_user, name='login-page'),
    path('register/', register_user, name='register-page'),
    path('logout/', logout_user, name='logout'),
    path('profile/', profile, name='profile')
]
