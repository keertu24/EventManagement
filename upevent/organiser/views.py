from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Organiser index")

def login(request):
    return HttpResponse("login of organiser")

def bookView(request):
    return HttpResponse("bookview of organiser")
