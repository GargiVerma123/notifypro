# inventory1/urls.py
from django.urls import path
from .views import InventoryAPIView

urlpatterns = [
    path('inventory/', InventoryAPIView.as_view(), name='inventory-list-create'),  # For GET and POST
    path('inventory/<int:id>/', InventoryAPIView.as_view(), name='inventory-detail'),  # For GET, PUT, DELETE (with id)
]
