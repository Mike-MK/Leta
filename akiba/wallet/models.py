# Create your models here.
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Account(models.Model):
    user = models.ForeignKey('auth.User',on_delete=models.CASCADE) 
    account_no = models.CharField(null=False,unique=True,max_length=20)
    balance = models.DecimalField(max_digits=6, decimal_places=2,default=0)

class Transaction(models.Model):
    account = models.ForeignKey('Account',on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
