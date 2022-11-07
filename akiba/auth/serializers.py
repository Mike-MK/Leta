from rest_framework import serializers
from django.contrib.auth.models import User
from wallet.serializers import AccountSerializer
from wallet.models import Account

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)

    def validate_password(self, value):
        if len(value) < 6:
            raise serializers.ValidationError("Password is too short")
        return value

    def create(self, validated_data):
        user = User.objects.create_user( 
            username=validated_data['username'],
            password=validated_data['password']
        )
        user.save()
        return user

    class Meta:
        model = User
        fields = ['id','username','password']
    