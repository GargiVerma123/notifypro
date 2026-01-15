"""
URL configuration for notifypro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path,include
from user.views import UserAPIView, LoginAPI
from customer.views import CustomerAPIView 
from inventory.views import InventoryAPIView
from lead.views import LeadAPIView
from list.views import ListAPIView

urlpatterns = [
    path('user/', UserAPIView.as_view()),
    path('customer/', CustomerAPIView.as_view()),
    path('inventory/', InventoryAPIView.as_view()),
    path('inventory1/', InventoryAPIView.as_view()),
    path('customer1/', CustomerAPIView.as_view()),
    path('lead/', LeadAPIView.as_view()),
    path('list/', ListAPIView.as_view()),
]
 
    