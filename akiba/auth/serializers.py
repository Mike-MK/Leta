from rest_framework import serializers
from django.contrib.auth.models import User
from wallet.serializers import AccountSerializer
from wallet.models import Account

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)
    account = AccountSerializer(many=True)

    def validate_password(self, value):
        if len(value) < 6:
            raise serializers.ValidationError("Password is too short")
        return value
    class Meta:
        model = User
        fields = ['id','username','password','account']
    def create(self, validated_data):
        account_data = validated_data.pop('account')
        print('acc3erar',account_data)
        user = User.objects.create(**validated_data)
        
        Account.objects.create(user=user, **account_data)
        return user