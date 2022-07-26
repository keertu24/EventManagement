from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'upevents/index.html')

def aboutUs(request):
    return render (request,'upevents/about.html')

def login(request):
    # user login page
    return render(request,'upevents/userlogin.html')

def confirmlogin(request):
    #it will confirm that is authecate user
    return HttpResponse("user login")

def signUp(request):
    #Just template to show the signup page
   return render(request,'upevents/usersignup.html')

def confirmsignUp(request):
    #end point to add a user
    return HttpResponse("user signup")

def organiserlogin(request):
    return HttpResponse("organiser login")