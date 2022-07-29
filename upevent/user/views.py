from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request ,'user/home.html')

def eventView(request):
    return  render(request ,'user/eventview.html')

def cart(request):
    return render(request ,'user/cart.html')

def userprofile(request):
    user_account=request.user
    user_id=user_account.id
    print(user_account)
    print(user_id)
    
    return render(request ,'user/userprofile.html')

def aboutUs(request):
    return render(request ,'upevents/aboutus.html')

def editprofile(request):
    return render(request ,'user/editprofile.html')

def confirmeditprofile(request):
    return HttpResponse(' confirm edittt')