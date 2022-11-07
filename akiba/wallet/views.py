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


class Account(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self,request):
        serialized = AccountSerializer(data=request.data) 
        user  = request.user 

        if serialized.is_valid():
            try:
                account = Account(
                    user = user,
                    account_no = serialized.data['account_no'],
                )
                
                return Response(serialized.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                print(e)
                return Response("Account already exists",status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)


class Deposit(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        try:
            user = request.user
            account = Account.objects.get(user=user)
            res = {
                'name':user.username,
                'balance':account.balance,
                'phone':account.phone,
            }
            return Response(res,status=200)
        except:
            return Response('Error',status=400)


    def post(self,request):
        
        amount = request.data.get('amount')       
        token = get_mpesa_auth_token()
        if not type(token)==str:
            return Response(status=status.HTTP_400_BAD_REQUEST,data={'message':'Auth Error'})
        
        content = {
            'amount':amount,
        }
        url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        code = "174379"
        key = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"
        phone = "254716537782"

        pwd = code+key+timestamp
        pwd_bytes = pwd.encode('ascii')
        pwd_b64_bytes = b64encode(pwd_bytes)
        b64_pwd = pwd_b64_bytes.decode('ascii')
        print(b64_pwd)
        # raise Exception()
        payload = {
            "BusinessShortCode": code,
            "Password": b64_pwd,
            "Timestamp": timestamp,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": "1",
            "PartyA": phone,
            "PartyB": code,
            "PhoneNumber": phone,
            "CallBackURL": "https://b924-102-140-246-229.ngrok.io/wallet/result/",
            "AccountReference": phone,
            "TransactionDesc": "Akiba Pay"
        }
        headers = {
            "Authorization": f"Bearer {token}",
        }
        response = requests.request("POST", url, json=payload, headers=headers)
        print(response.text)
        # raise Exception()
        return Response(content)


class MpesaCallback(APIView):
    def post(self,request):
        print("-------call back called--------------")
        
        return Response("Transaction successful",status=status.HTTP_202_ACCEPTED)
