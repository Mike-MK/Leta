from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/',include('auth.urls')),
    path('wallet/',include('wallet.urls')),
]
