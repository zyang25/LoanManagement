from django.shortcuts import render
from rest_framework.views import APIView
from account.models import Account
from .models import Customer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from .permissions import IsOwner
from .serializers import CustomerSerializer
from rest_framework import status

# Create your views here.
class ListCustomer(APIView):

    permission_classes = (IsAuthenticated, IsOwner)

    def get(self, request, format=None):
        
        customer_list = Customer.objects.filter(account_customer=request.user)

        ser = CustomerSerializer(customer_list, many=True)

        return Response(ser.data)

    def post(self, request, format=None):

        ser = CustomerSerializer(data=request.data)
        if ser.is_valid():
            ser.save(account_customer=self.request.user)
            return Response(ser.data, status.HTTP_201_CREATED)
        return Response(ser.errors, status.HTTP_400_BAD_REQUEST)

class CustomerDetail(APIView):

    permission_classes = (IsAuthenticated, IsOwner)

    def get_customer(self, id):
        customer = Customer.objects.get(pk)
        return customer

    def get(self, request, id):
        c = self.get_customer(pk)
        ser = CustomerSerializer(c)
        return Response(ser.data)

    def put(self, request, id, format=None):
        customer = Customer.objects.get(id=id)
        ser = CustomerSerializer(customer, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        else:
            return Response(ser.errors)
    
    def delete(self, request, id, format=None):
        c = Customer.objects.get(pk=id)
        c.delete()
        return Response({}, status.HTTP_204_NO_CONTENT)


