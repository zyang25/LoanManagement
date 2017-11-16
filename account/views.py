from django.shortcuts import render
from .models import Account
from .serializers import AccountSerializer
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
# Create your views here.

class AccountView(viewsets.ViewSet):
    permission_classes = (AllowAny,)
    
    def registration(self, request):
        ser = AccountSerializer(data=request.data)

        if ser.is_valid():
            account = ser.save()
            if account:
                return Response(ser.data, status.HTTP_201_CREATED)
        else:
            return Response({"StatusCode":"2", "Message": ser.errors}, status.HTTP_400_BAD_REQUEST)
    
    def verify(self, uuid):
        account = None
        try:
            account = Account.objects.filter(verification_uuid=uuid, is_verified=False)
            account.is_verified = True
            ser = AccountSerializer(account)
            if ser.is_valid():
                ser.save()
                return Response({"StatusCode":"0", "Message": ser.data}, status.HTTP_201_CREATED)
        except:
            return Response({"StatusCode":"1", "Message": ser.errors}, status.HTTP_400_BAD_REQUEST)


def verify(self, request, uuid):
    
    if request.method == 'POST':
        account = None
        try:
            account = Account.objects.filter(verification_uuid=uuid, is_verified=False)
            account.is_verified = True
            ser = AccountSerializer(account)
            if ser.is_valid():
                ser.save()
                return Response({"StatusCode":"0", "Message": ser.data}, status.HTTP_201_CREATED)
        except:
            return Response({"StatusCode":"1", "Message": ser.errors}, status.HTTP_400_BAD_REQUEST)


