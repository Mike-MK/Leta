from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from wallet.models import *
from .serializers import *

# Create your views here.
class Register(APIView):
    def post(self,request):   
        serialized = UserSerializer(data=request.data)
        
        if serialized.is_valid():
            try:
                user = User.objects.create_user(
                serialized.data['username'],
                serialized.data['password']
                )
                
                return Response(user.username, status=status.HTTP_201_CREATED)
            except:
                return Response("User already exists",status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)
            # try:
            #     username = request.data.get('username')
            #     password = request.data.get('password')
            #     phone = request.data.get('phone')

            #     user = User.objects.create_user(username, password=password)
            #     account =  Account(
            #         user = user,
            #         balance = 0,
            #         account_no = phone,
            #     )
            #     account.save()
            #     return Response(status=status.HTTP_201_CREATED,data={
            #         'msg': "Success",
            #         'user': user.username,
            #         'balance': account.balance,
            #         'account_no': account.account_no,
            #         })
            # except Exception:
            #     return Response(status=status.HTTP_400_BAD_REQUEST)

        
        
