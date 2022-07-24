from django.contrib import admin
from django.urls import path
from . import  views

urlpatterns = [
    path('',views.index,name="userindex"),
    
    path('forgotpassword',views.forgotPass,name='userforgot'),
    path('eventview/', views.eventView, name='usereventview'),
    path('cart/',views.cart,name='cart'),
    path("profile/",views.profile,name="profile"),
    
    
]