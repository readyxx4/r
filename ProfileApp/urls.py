from django.urls import path
from .views import user_login, user_logout
from . import views

urlpatterns = [
    path('login', views.user_login, name='user_login'),
    path('logout', user_logout, name='user_logout'),
    path('home', views.home, name='home'),
    path('stock', views.stock, name='stock'),
    path('product/productList', views.productList, name='productList'),
    path('product/computerList', views.computerList, name='computerList'),
    path('product/computerOne/<cid>', views.computerOne, name='computerOne'),
    path('product/categoryList', views.categoryList, name='categoryList'),
]
