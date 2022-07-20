from django.contrib import admin
from django.urls import path
from . import  views

urlpatterns = [
    path('',views.index,name="userindex"),
    path('login/', views.login, name='userLogin'),
    path('signup/',views.signUp,name='userSignUp'),
    path('forgotpassword',views.forgotPass,name='userforgot'),
    path('eventview/', views.eventView, name='usereventview'),
    path('cart/',views.cart,name='cart'),
    path("profile/",views.profile,name="profile"),
    path('aboutus/',views.aboutUs,name='aboutUs')
]