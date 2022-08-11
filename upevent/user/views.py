
from datetime import date
from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from organiser.models import Event,Package
from user.function import usercartproduct
from user.models import UserProfile
from user.models import Cart,Order
from django.core.files.storage import FileSystemStorage
from django.template import context
import json 
from user.function import usercart
import re

order_amount=0
# Create your views here.
def home(request):
    events=Event.objects.all()
    return render(request,'user/home.html',{'events':events})

def eventView(request):
    # this variable to store list of package 
    allpack=[]
    # saving the packages in category wise 
    catpack=Package.objects.values('category','package_id')
    cats={item['category'] for item in catpack}
    for cat in cats:
        prod=Package.objects.filter(category=cat).order_by('category')
        allpack.append(prod)
    return  render(request ,'user/eventview.html',{'allpack':allpack})

def cart(request):
    owner=request.user
    # user_cart=Cart.objects.filter(user_name=owner)# getting list of the selected items in cart
    # user_cart_items=[]# it saves the id of each cart item and also to get only some value 
    select_pack_to_template=usercartproduct(owner)# it send the selected item information that store in the package table 
    # for i in user_cart:
    #     user_cart_items=i.food_choice,i.music_choice,i.stage_choice,i.decor_choice,i.light_choice #selecting only 5 items and avoiding rest of details 
    # for i in user_cart_items:
    #     user_cart_items_selected=Package.objects.filter(package_id=i)
    #     select_pack_to_template.append(user_cart_items_selected)#appending to list of item 
    # cart_items=user_cart_items
    return render(request ,'user/cart.html',{'user_cart':select_pack_to_template})

def userprofile(request):
    dateoftoday=date.today()
    order_items_over=Order.objects.filter(user_name=request.user,date__lte=dateoftoday).order_by('date')
    order_items_coming=Order.objects.filter(user_name=request.user,date__gt=dateoftoday).order_by('date')
    userprofile=UserProfile.objects.filter(user_name=request.user)
    return render(request ,'user/userprofile.html',{'user_image':userprofile,'order_items_over':order_items_over,'order_items_coming':order_items_coming})

def aboutUs(request):
    return render(request ,'upevents/aboutus.html')

def addprofile(request):
    return render(request ,'user/addprofile.html')

def confirmaddprofile(request):
    # try block must 
    try:
        if request.method=='POST' :
            owner=request.user
            mbl_no=request.POST.get('addprofilemblno')
            dob=request.POST.get('addprofiledob')
            gender=request.POST.get('addprofilegenderradio')
            user_image=request.FILES.get('profilepic')
            if len(mbl_no)!=10:
                messages.error(request,'Mobile Number must be 10 digits')
                return redirect('/user/addprofile')

            # handle the file url 
            if user_image:
                fs=FileSystemStorage()
                filename=fs.save(user_image.name, user_image)
                url =fs.url(filename)
                new_user_profile=UserProfile(user_name=owner,user_mbl_no=mbl_no,user_dob=dob,user_gender=gender,user_image=url)
                new_user_profile.save()
                messages.success(request,'Profile information successfully saved')
                return redirect('/user/userprofile')
            # saving information in UserProfile table 
            new_user_profile=UserProfile(user_name=owner,user_mbl_no=mbl_no,user_dob=dob,user_gender=gender)
            new_user_profile.save()
            messages.success(request,'Profile information successfully saved')
            return redirect('/user/userprofile')
        else:

            return HttpResponse(' 404-Not Found')
    except:
            messages.error(request,'Please use option edit profile, your profile information  added already')
            return redirect('/user/userprofile')

def editprofile(request):
    # sending enterred user information to templates 
    userprofile=UserProfile.objects.filter(user_name=request.user)
    return render(request ,'user/editprofile.html',{'userinfo':userprofile})

def confirmeditprofile(request):
    # try block must 
    if request.method=='POST':
        owner=request.user
        first_name=request.POST.get('editfname')
        last_name=request.POST.get('editlname')
        email=request.POST.get('editprofileemail')
        mbl_no=request.POST.get('editprofilemblno')
        dob=request.POST.get('editprofiledob')
        gender=request.POST.get('editprofilegenderradio')
        user_image=request.FILES.get('editprofilepic')
        if len(mbl_no)!=10:
                messages.error(request,'Mobile Number must be 10 digits')
                return redirect('/user/editprofile')
        try:
            # handling the image url 
            update_user_profile=UserProfile.objects.get(user_name=owner)
            if user_image:
                fs=FileSystemStorage()
                filename=fs.save(user_image.name, user_image)
                url =fs.url(filename)
                update_user_profile.user_image=url
            # saving update in User table 
            user=User.objects.get(id=owner.id)
            user.first_name=first_name
            user.last_name=last_name
            user.email=email
            user.save()
            # updating the UserProfile table 
            update_user_profile.user_mbl_no=mbl_no
            update_user_profile.user_dob=dob
            update_user_profile.user_gender=gender
            update_user_profile.save()
            messages.success(request,'Profile information successfully updated')
            return redirect('/user/userprofile')
        except:
            messages.error(request,'Please add information before editing it !!!!! ')
            return redirect('/user/userprofile')
    else:
        return HttpResponse(' 404-Not Found')

def submitpackage(request):
    # not dynamic its just static 
    if(request.method=='POST'):
        musicchoice=request.POST.get('MUSIC')
        foodchoice=request.POST.get('FOOD')
        decorchoice=request.POST.get('DECORATION')
        lightchoice=request.POST.get('LIGHTING')
        stagechoice=request.POST.get('STAGE PROGRAM')   
        # checking if atleast one item selected or not 
        if musicchoice==None and foodchoice==None and decorchoice==None and lightchoice==None and stagechoice==None :
            messages.error(request,'Please select atleast one item ')
            return redirect('/user')

        owner=request.user
        try:
            user_cart=Cart(user_name=owner,music_choice=musicchoice,food_choice=foodchoice,decor_choice=decorchoice,light_choice=lightchoice,stage_choice=stagechoice)
            user_cart.save()
            messages.success(request,'Cart Item Added Successfully ')
            return redirect('/user')
        except:
            messages.error(request,'Please Clear Your Cart Before Adding new item')
            return redirect('/user')
    else:
        return HttpResponse("404-Not Found")

def clearcart(request):
    owner=request.user 
    clearcart=Cart.objects.filter(user_name=owner)
    clearcart.delete()
    messages.success(request,'Cart cleared')
    return redirect('/user')

def checkout(request):
        owner=request.user
        # user_cart=Cart.objects.filter(user_name=owner)# getting list of the selected items in cart
        # user_cart_items=[]# it saves the id of each cart item and also to get only some value 
        select_pack_to_template=usercartproduct(owner=owner)# it send the selected item information that store in the package table 
        # for i in user_cart:
        #     user_cart_items=i.food_choice,i.music_choice,i.stage_choice,i.decor_choice,i.light_choice #selecting only 5 items and avoiding rest of details 
        # cart_items=user_cart_items
        #user_cart_items=usercart(owner)
        # for i in user_cart_items:
        #     user_cart_items_selected=Package.objects.filter(package_id=i)
        #     select_pack_to_template.append(user_cart_items_selected)#appending to list of item 
        sum=0# sum 0f all the amount in the packages 
        for i in select_pack_to_template:
            for j in i :
                sum=sum+j.package_price
        return render(request ,'user/checkout.html',{'user_cart':select_pack_to_template,'sum':sum})
   
    
def confirmcheckout(request):
    global order_amount
    # also check for empty cart items 
    if request.method=='POST':
        fname=request.POST.get('checkoutfname')
        lname=request.POST.get('checkoutlname')
        full_name=fname+" "+lname
        if not re.match("^[a-zA-Z\s]+$",full_name):
                messages.error(request, "Only Characters allowed in Name")
                return redirect('/user/checkout')

        mbl_no=request.POST.get('checkoutmblno')
        
        if len(mbl_no)!=10:
            messages.error(request, "Mobile numbers must be 10 digits")
            return redirect('/user/checkout')

        venue_pin=request.POST.get('checkoutpin')
        if len(venue_pin)!=6 :
            messages.error(request, "Pin code must be 6 digits")
            return redirect('/user/checkout')

        order_amount=request.POST.get('estcost')
        invite_pic=request.FILES.get('checkoutpic')
        fs=FileSystemStorage()
        filename=fs.save(invite_pic.name, invite_pic)
        url =fs.url(filename)
        owner=request.user
        cart_items=usercart(owner=owner)
        # Adding records to the order table 
        order_object=Order(user_name=owner,name=full_name,
        mbl_no=mbl_no,
        email=request.POST.get('checkoutemail'),
        date=request.POST.get('checkoutdate'),
        time=request.POST.get('checkouttime'),
        est_people=request.POST.get('checkoutpeople'),
        venue=request.POST.get('checkoutvenue'),
        venue_address=request.POST.get('checkoutaddress'),
        venue_pin=venue_pin,
        est_cost=request.POST.get('estcost'),invite_image=url,
        order_items=json.dumps(cart_items)
        )
        order_object.save()
        clearcart=Cart.objects.filter(user_name=owner)
        clearcart.delete()
        messages.success(request,'Order Placed')
        return redirect('/user/orderplace')
    else:
        return HttpResponse("404-Not found")

def orderplace(request):
    global order_amount
    return render(request,'user/orderplaced.html',{'order_amount':order_amount})

def orderinfo(request,order_id):
    order_details=Order.objects.filter(order_id=order_id)
    for i in order_details:
        order_item_list=json.loads(i.order_items)
    package_object=[]# list contain ordered package details 
    for i in order_item_list:
        package_object.append(Package.objects.filter(package_id=i))
    return render(request,'user/orderinfo.html',{'order_details':order_details,'order_item_list': package_object})

def orderdelete(request,order_id):
    order=Order.objects.get(order_id=order_id)
    order.delete()
    messages.success(request,'Order deleted')
    return redirect('/user/userprofile')
