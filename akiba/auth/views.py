from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from wallet.models import *
from .serializers import *


# Create your views here.
class Register(APIView):
    def post(self,request):   
        serializer_class = UserSerializer(data=request.data)
        account_serializer = AccountSerializer(data=request.data)

        # print('data',request.data["account_no"])
        
        if serializer_class.is_valid():
            # user = serializer_class.save()
            # account_serializer.is_valid()
           
            # account = account_serializer.save(user=user)
            user = User.objects.create(
                username=serializer_class.data['username'],
                password=serializer_class.data['password'],
                account=serializer_class.data['account']
            )
            # try:
            #     user = User.objects.create_user(
            #     username=serialized.data['username'],
            #     password=serialized.data['password'],
            #     account=serialized.data['account']
            #     )

            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
            # except:
            #     return Response("User already exists",status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer_class._errors, status=status.HTTP_400_BAD_REQUEST)
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

        
        
