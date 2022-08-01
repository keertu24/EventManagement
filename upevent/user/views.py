from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from organiser.models import Event,Package
from user.models import Cart
from django.template import context

allcategory=[]
# Create your views here.
def home(request):
    events=Event.objects.all()
    print(events)
    return render(request,'user/home.html',{'events':events})

def eventView(request):
    # this variable to store list of package 
    global allcategory
    allpack=[]
    catpack=Package.objects.values('category','package_id')
    cats={item['category'] for item in catpack}
    for cat in cats:
        prod=Package.objects.filter(category=cat)
        allpack.append(prod)
    
    return  render(request ,'user/eventview.html',{'allpack':allpack})

def cart(request):
    owner=request.user
    user_cart=Cart.objects.filter(user_name=owner)
    user_cart_items=[]
    select_pack_to_template=[]
    for i in user_cart:
        user_cart_items=i.food_choice,i.music_choice,i.stage_choice,i.decor_choice,i.light_choice
    print(user_cart_items)
    for i in user_cart_items:
        user_cart_items_selected=Package.objects.filter(package_id=i)
        print(user_cart_items_selected)
        select_pack_to_template.append(user_cart_items_selected)
    return render(request ,'user/cart.html',{'user_cart':select_pack_to_template})

def userprofile(request):
    user_account=request.user
    user_id=user_account.id
    print(user_account)
    print(user_id)
    
    return render(request ,'user/userprofile.html')

def aboutUs(request):
    return render(request ,'upevents/aboutus.html')

def addprofile(request):
    return render(request ,'user/addprofile.html')

def confirmaddprofile(request):
    return HttpResponse(' confirm edittt')

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