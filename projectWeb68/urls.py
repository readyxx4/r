"""
URL configuration for projectWeb68 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from .views import home
from .views import login
from ProfileApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', include('ProfileApp.urls')),
    path('', login, name='login'),
    path('home/',home, name='home'),  
    path('stock', views.stock, name='stock'),
    path('product/productList', views.productList, name='productList'),
    path('product/computerList', views.computerList, name='computerList'),    
    path('product/computerOne<cid>', views.computerOne, name='computerOne'),
    path('product/categoryList/', views.categoryList, name='categoryList'),   
]
