from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request ,'user/index.html')

def login(request):
    return HttpResponse("user login")

def signUp(request):
    return HttpResponse("user signup")

def forgotPass(request):
    return HttpResponse("user forgotpass")

def eventView(request):
    return HttpResponse("user eventView")

def cart(request):
    return HttpResponse("user cart")

def profile(request):
    return HttpResponse("user profile")

# def aboutUs(request):
    # return HttpResponse("user aboutUs")
