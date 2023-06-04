"""shopping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from django.urls import path
from .views import *


urlpatterns = [
    path('',store,name='store'),
    path('checkout/',checkout,name='checkout'),
    path('cart/',cart,name='cart'),
    path('aboutus/',aboutus_page,name='about_us'),
    path('contactus/',contactus_page,name='contact_us'),
    path('store/<slug:slug>',product_detail,name='product_detail'),
    # this is to add product in cart 
    path('cart/<int:pk>',cartadd , name='cartadd'),
    




]
