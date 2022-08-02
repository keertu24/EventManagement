
from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from organiser.models import Event,Package
from user.models import UserProfile
from user.models import Cart
from django.core.files.storage import FileSystemStorage
from django.template import context


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
        prod=Package.objects.filter(category=cat)
        allpack.append(prod)
    return  render(request ,'user/eventview.html',{'allpack':allpack})

def cart(request):
    owner=request.user
    user_cart=Cart.objects.filter(user_name=owner)# getting list of the selected items in cart
    user_cart_items=[]# it saves the id of each cart item and also to get only some value 
    select_pack_to_template=[]# it send the selected item information that store in the package table 
    for i in user_cart:
        user_cart_items=i.food_choice,i.music_choice,i.stage_choice,i.decor_choice,i.light_choice #selecting only 5 items and avoiding rest of details 
    for i in user_cart_items:
        user_cart_items_selected=Package.objects.filter(package_id=i)
        select_pack_to_template.append(user_cart_items_selected)#appending to list of item 
    return render(request ,'user/cart.html',{'user_cart':select_pack_to_template})

def userprofile(request):
    userprofile=UserProfile.objects.filter(user_name=request.user)
    return render(request ,'user/userprofile.html',{'user_image':userprofile})

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
            # handle the file url 
            if user_image:
                fs=FileSystemStorage()
                filename=fs.save(user_image.name, user_image)
                url =fs.url(filename)
                new_user_profile=UserProfile(user_name=owner,user_mbl_no=mbl_no,user_dob=dob,user_gender=gender,user_image=url)
                new_user_profile.save()
            # saving information in UserProfile table 
            new_user_profile=UserProfile(user_name=owner,user_mbl_no=mbl_no,user_dob=dob,user_gender=gender)
            new_user_profile.save()
            return redirect('/user/userprofile')
        else:

            return HttpResponse(' 404-Not Found')
    except:
            messages.error(request,'Please use option edit profile, your profile information  added already and also check the mobile no')
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
        user_image=request.POST.get('editprofilepic')
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
        print('Music',musicchoice)
        print('Food',foodchoice)
        print('Decor',decorchoice)
        print('light',lightchoice)
        print('Stage',stagechoice)
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
    user_cart=Cart.objects.filter(user_name=owner)# getting list of the selected items in cart
    user_cart_items=[]# it saves the id of each cart item and also to get only some value 
    select_pack_to_template=[]# it send the selected item information that store in the package table 
    for i in user_cart:
        user_cart_items=i.food_choice,i.music_choice,i.stage_choice,i.decor_choice,i.light_choice #selecting only 5 items and avoiding rest of details 
    for i in user_cart_items:
        user_cart_items_selected=Package.objects.filter(package_id=i)
        select_pack_to_template.append(user_cart_items_selected)#appending to list of item 
    return render(request ,'user/checkout.html',{'user_cart':select_pack_to_template})
    