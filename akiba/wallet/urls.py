from django.urls import path
from . import views
  
urlpatterns = [
    path('hello', views.HelloView.as_view(), name ='hello'),
    path('', views.Deposit.as_view()),
    path('result', views.MpesaCallback.as_view()),
]