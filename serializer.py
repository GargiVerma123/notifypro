from rest_framework import serializers
from .models import List, Customer

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = ['id', 'customer', 'address']

class CustomerSerializer(serializers.ModelSerializer):
    addresses = ListSerializer(many=True, read_only=True)
    
    class Meta:
        model = Customer
        fields = ['id', 'customer_id', 'name', 'addresses']
