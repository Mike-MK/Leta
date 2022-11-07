from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.test.client import Client
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
from .models import *
from rest_framework import status

class AccountTests(APITestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        

    def test_create_account(self):
        self.client.login(username='john', password='johnpassword')
        url = reverse('account')
        data = {'account_no': '254716537782'}
        response = self.client.post(url, data, format='json')
        print(response.text)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Account.objects.count(), 1)
        self.assertEqual(Account.objects.get().account_no,'254716537782')