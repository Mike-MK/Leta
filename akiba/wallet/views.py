from base64 import b64decode, encode,b64encode
from sqlite3 import Timestamp
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import requests
from datetime import datetime
import json

class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self,request):
        content = {'message' : 'Hello'}
        return Response(content)
    
class Deposit(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        response = requests.request("POST","https://882c-102-140-246-229.ngrok.io/wallet/result")
        print("callback")
        print(response.text)
        return Response


    def post(self,request):
        amount = request.data.get('amount')
        consumer_key = "DBKT6n6IXsxGt1vwueGB1pygGrlII1PX"
        consumer_secret =  "jGJA828Jt97lP9k0"
        key_secret = consumer_key+":"+consumer_secret

        bytes = key_secret.encode('ascii')
        b64_bytes = b64encode(bytes)
        b64_token = b64_bytes.decode('ascii')
        
        # raise Exception()
        auth_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate"
        querystring = {"grant_type":"client_credentials"}
        payload = ""
        headers = {
            "Authorization": f"Basic {b64_token}"
        }
        response = requests.request("GET", auth_url, data=payload, headers=headers, params=querystring)
        # print(response.text)
       
        content = {
            'amount':amount,
            'response': response.text
        }
        token = json.loads(response.text)['access_token']
        # print(token)
        
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
            "CallBackURL": "https://382e-102-140-246-229.ngrok.io/wallet/result",
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
        return Response("Callback called")
