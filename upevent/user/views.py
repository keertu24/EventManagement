from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request ,'user/home.html')

def eventView(request):
    return HttpResponse("user eventView")

def cart(request):
    return render(request ,'user/cart.html')

def userprofile(request):
    user_account
    return render(request ,'user/userprofile.html')

def aboutUs(request):
    return render(request ,'upevents/aboutus.html')
