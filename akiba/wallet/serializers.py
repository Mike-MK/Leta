from rest_framework import serializers
from .models import *

class AccountSerializer(serializers.ModelSerializer):
    account_no = serializers.CharField(max_length=20)

    def validate_account_no(self, value):
        if len(value) < 12:
            raise serializers.ValidationError("Phone number is invalid")
        return value
    class Meta:
        model = Account
        fields = ('account_no',)