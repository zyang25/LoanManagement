from rest_framework import serializers
from .models import Customer
class CustomerSerializer(serializers.ModelSerializer):
    
    #owner = serializers.ReadOnlyField(source='account.email') # ADD THIS LINE
    #account_customer = serializers.ReadOnlyField(source='account')

    def create(self, validated_data):
        #print(validated_data)
        return Customer.objects.create(**validated_data)
    
    class Meta:
        model = Customer
        fields = ('account_customer', 'fullname', 'cell', 'created')
