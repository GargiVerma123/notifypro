# leads/serializers.py
from rest_framework import serializers
from .models import Lead

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ['customer_id', 'name', 'phone', 'email', 'summary', 'status']
