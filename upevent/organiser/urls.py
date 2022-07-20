from django.contrib import admin
from django.urls import path
from . import  views

urlpatterns = [
    path('',views.index,name='organiserindex'),
    path('login/',views.login,name='organiserLogin'),
    path('forgotpassword',views.forgotPass,name='userforgot'),
    path('bookview',views.bookView,name='organiserview')
]