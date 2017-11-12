from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=Account.objects.all())]
            )
    password = serializers.CharField(min_length=6)

    # validated_data contains all the validated data
    def create(self, validated_data):
        return Account.objects.create_user(validated_data['email'], validated_data['password'])

    class Meta:
        model = Account
        fields = ('email', 'password')

