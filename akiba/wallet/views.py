from base64 import b64decode, encode,b64encode
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
import requests
from datetime import datetime
import json
from .models import Account
from .utils import *
from .serializers import *
from django.core.exceptions import ObjectDoesNotExist


class Account(APIView):
    # check jwt token
    permission_classes = (IsAuthenticated,)

    # create new account
    def post(self,request):
        # serialize request data to object
        serializer = AccountSerializer(data=request.data) 
        user  = request.user 

        # check request data is valid
        if serializer.is_valid():
            try:
                serializer.save(user=user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                print(e)
                return Response({"message":"Account already exists"},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)

    # get account details
    def get(self,request):
        user = request.user
        try:        
            account = Account.objects.get(user=user)
            res = {
                'message':'User retrieved',
                'name':user.username,
                'balance':account.balance,
                'phone':account.phone,
            }
            return Response(res,status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({'message':'User Account Not Found'},status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'message':'Error retrieving user'},status=status.HTTP_400_BAD_REQUEST)


class Deposit(APIView):
    # check jwt token
    permission_classes = (IsAuthenticated,)
    
    def post(self,request):        
        amount = request.data.get('amount')
         
        # get auth token with consumer secret and password        
        token = get_mpesa_auth_token()
        if not type(token)==str:
            return Response(status=status.HTTP_400_BAD_REQUEST,data={'message':'Authentication Error'})
        
        url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"

        # stk push request body
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        code = "174379"
        key = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"
        phone = "254716537782"
        
        # pwd + passkey + timestamp to base64
        pwd = code+key+timestamp
        pwd_bytes = pwd.encode('ascii')
        pwd_b64_bytes = b64encode(pwd_bytes)
        b64_pwd = pwd_b64_bytes.decode('ascii')

        payload = {
            "BusinessShortCode": code,
            "Password": b64_pwd,
            "Timestamp": timestamp,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": code,
            "PhoneNumber": phone,
            "CallBackURL": "https://a294-197-232-124-42.ngrok.io:80/wallet/result/",
            "AccountReference": phone,
            "TransactionDesc": "Akiba Pay"
        }
        headers = {
            "Authorization": f"Bearer {token}",
        }

        # stk push request
        response = requests.request("POST", url, json=payload, headers=headers)
        if response.status_code == 200:
            return Response({"message":"Success"})
        else:
            return Response({"message":"Error"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ResultCallback(APIView):
    def post(self,request):
        print("-------call back called--------------")
        
        return Response("Transaction successful",status=status.HTTP_202_ACCEPTED)
