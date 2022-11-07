from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from wallet.models import *
from .serializers import *


# Create your views here.
class Register(APIView):
    def post(self,request):   
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = serializer.save()
                return Response({'id':user.id}, status=status.HTTP_201_CREATED)
            except:
                return Response("User already exists",status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)
            