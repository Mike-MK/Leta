from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)

    def validate_password(self, value):
        if len(value) < 6:
            raise serializers.ValidationError("Password is too short")
        return value
    class Meta:
        model = User
        fields = ('id','username','password')