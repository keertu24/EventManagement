from django.contrib import admin
from django.urls import path
from . import  views

urlpatterns = [
    path('',views.home,name="userhome"),
    path('eventview/', views.eventView, name='usereventview'),
    path('cart/',views.cart,name='cart'),
    path('userprofile/',views.userprofile,name="userprofile"),
    
    
]