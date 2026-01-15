from django.urls import path
from .views import ListAPIView

urlpatterns = [
    path('addresses/', ListAPIView.as_view(), name='address-list'),  # List all addresses or create new
    path('addresses/<str:customer_id>/', ListAPIView.as_view(), name='address-detail'),  # Get, update, or delete by customer_id
]
