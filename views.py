from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import List
from .serializers import ListSerializer

class ListAPIView(APIView):
    # Create a new address record for a customer
    def post(self, request):
        serializer = ListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Retrieve a list of all address records, or a specific address by customer_id
    def get(self, request, customer_id=None):
        if customer_id:
            try:
                address = List.objects.get(customer_id=customer_id)
            except List.DoesNotExist:
                return Response({"error": "Address Not Found"}, status=status.HTTP_404_NOT_FOUND)
            serializer = ListSerializer(address)
            return Response(serializer.data)
        
        # Get all address records
        addresses = List.objects.all()
        serializer = ListSerializer(addresses, many=True)
        return Response(serializer.data)

    # Update the address record for a specific customer
    def put(self, request, customer_id):
        try:
            address = List.objects.get(customer_id=customer_id)
        except List.DoesNotExist:
            return Response({"error": "Address Not Found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ListSerializer(address, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete a specific address record by customer_id
    def delete(self, request, customer_id):
        try:
            address = List.objects.get(customer_id=customer_id)
        except List.DoesNotExist:
            return Response({"error": "Address Not Found"}, status=status.HTTP_404_NOT_FOUND)
        
        address.delete()
        return Response({"message": "Address Deleted"}, status=status.HTTP_204_NO_CONTENT)
