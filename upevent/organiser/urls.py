from django.contrib import admin
from django.urls import path
from . import  views

urlpatterns = [
    path('',views.index,name='organiserindex'),
    path('userorderinfo/<int:order_id>',views.userorderinfo,name='userorderinfo'),
    path('addnews/',views.addnews,name='addnews'),
    path('viewpackage/',views.viewpackage,name='viewpackage'),
    path('confirmnews/',views.confirmnews,name='confirmnews'),
    path('viewquery/',views.viewquery,name='viewquery')
]