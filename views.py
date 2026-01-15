# leads/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Lead
from .serializers import LeadSerializer

class LeadAPIView(APIView):
    def post(self, request):
        serializer = LeadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, customer_id=None):
        if customer_id:
            try:
                lead = Lead.objects.get(customer_id=customer_id)
            except Lead.DoesNotExist:
                return Response({"error": "Lead Not Found"}, status=status.HTTP_404_NOT_FOUND)
            serializer = LeadSerializer(lead)
            return Response(serializer.data)
        leads = Lead.objects.all()
        serializer = LeadSerializer(leads, many=True)
        return Response(serializer.data)

    def put(self, request, customer_id):
        try:
            lead = Lead.objects.get(customer_id=customer_id)
        except Lead.DoesNotExist:
            return Response({"error": "Lead Not Found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = LeadSerializer(lead, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, customer_id):
        try:
            lead = Lead.objects.get(customer_id=customer_id)
        except Lead.DoesNotExist:
            return Response({"error": "Lead Not Found"}, status=status.HTTP_404_NOT_FOUND)
        lead.delete()
        return Response({"message": "Lead Deleted"}, status=status.HTTP_204_NO_CONTENT)
