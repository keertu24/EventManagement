from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    if(request.user.is_staff):
        return render(request,'organiser/index.html')
    else:
        return HttpResponse('404-Not Found')
def login(request):
    return HttpResponse("login of organiser")

def forgotPass(request):
    return HttpResponse("forgot password for org")

def bookView(request):
    return HttpResponse("bookview of organiser")
