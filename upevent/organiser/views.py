

from django.shortcuts import render,redirect
from django.contrib import messages


# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from organiser.models import Organiser,Package,Contact
from user.models import Order
from datetime import date
import json
from organiser.form import NewsForm


# Create your views here.
def index(request):
    organiser=Organiser.objects.filter(username=request.user)
    if request.user.is_staff and organiser:
        orders=Order.objects.filter(date__gt=date.today()).order_by('date')
        context={'organiser':organiser,'orders':orders}
        return render(request,'organiser/index.html',context)
    else:
        return HttpResponse('404-Not Found')

def userorderinfo(request,order_id):
    order_details=Order.objects.filter(order_id=order_id)
    for i in order_details:
        order_item_list=json.loads(i.order_items)
    package_object=[]# list contain ordered package details 
    for i in order_item_list:
        package_object.append(Package.objects.filter(package_id=i))
    return render(request,'organiser/userorderinfo.html',{'order_details':order_details,'order_item_list': package_object})

def addnews(request):
    form=NewsForm
    context={'form':form}
    return render(request,'organiser/addnews.html',context)

def confirmnews(request):
    if request.method=='POST':
        form=NewsForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'News added in the database')
            return redirect('/organiser')
        else:
            return HttpResponse('not valid data')

def viewpackage(request):
    allpack=[]
    # saving the packages in category wise 
    catpack=Package.objects.values('category','package_id')
    cats={item['category'] for item in catpack}
    for cat in cats:
        prod=Package.objects.filter(category=cat)
        allpack.append(prod)
    return  render(request ,'organiser/viewpackage.html',{'allpack':allpack})

def viewquery(request):
    query=Contact.objects.all()
    return render(request,'organiser/viewquery.html',{'query':query})
    
