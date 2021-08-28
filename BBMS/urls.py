"""BBMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from BBM.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', About, name='about'),
    path('frontpage/', frontpage,  name='frontpage'),
    path('request/', request, name='request'),
    path('search/', search, name='search'),
    path('donorform/', donorform, name='donorform'),
    path('get_donors_list/', get_donors_list, name='get_donors_list'),


]
