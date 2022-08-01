from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import  views

urlpatterns = [
    path('',views.home,name="userhome"),
    path('eventview/', views.eventView, name='usereventview'),
    path('cart/',views.cart,name='cart'),
    path('userprofile/',views.userprofile,name="userprofile"),
    path('addprofile/',views.addprofile,name='addprofile'),
    path('confirmaddprofile/',views.confirmaddprofile,name='confirmaddprofile'),
    path('submitpackage/',views.submitpackage,name='submitpackage'),
    path('clearcart/',views.clearcart,name='clearcart')
    
    
]