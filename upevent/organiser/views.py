from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'organiser/index.html')

def login(request):
    return HttpResponse("login of organiser")

def forgotPass(request):
    return HttpResponse("forgot password for org")

def bookView(request):
    return HttpResponse("bookview of organiser")
