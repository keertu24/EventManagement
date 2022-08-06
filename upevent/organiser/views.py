from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from organiser.models import Organiser,Package
from user.models import Order
from datetime import date
import json


# Create your views here.
def index(request):
    organiser=Organiser.objects.filter(username=request.user)
    if request.user.is_staff and organiser:
        orders=Order.objects.filter(date__gt=date.today()).order_by('date')
        print(orders)


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
    
