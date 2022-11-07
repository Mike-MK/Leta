from django.urls import path
from . import views
  
urlpatterns = [
    path('', views.Deposit.as_view()),
    path('account', views.Account.as_view(),name='account'),
    path('result', views.ResultCallback.as_view()),
]