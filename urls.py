"""
URL configuration for cropproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from operator import index
from django.contrib import admin
from django.urls import path
from cropyield.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',index,name='index'),
    path('farmer/',farmer,name='farmer'),
    path('investor/',investor,name='investor'),
    path('flogin/',flogin,name='flogin'),
    path('ilogin/',ilogin,name='ilogin'),
    path('fmain/',fmain,name='fmain'),
    path('fresult/',fresult,name='fresult'),
    path('imain/',imain,name='imain'),
    path('iresult/',iresult,name='iresult'),
]
