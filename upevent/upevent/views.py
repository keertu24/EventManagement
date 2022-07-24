from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'upevents/index.html')

def aboutUs(request):
    return render (request,'upevents/about.html')

def login(request):
    return HttpResponse("user login")

def signUp(request):
    return HttpResponse("user signup")

def organiserlogin(request):
    return HttpResponse("organiser login")