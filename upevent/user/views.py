from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from organiser.models import Event,Package
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
    radio=request.POST['radio']
    print(radio)
    return render(request ,'user/cart.html')

def userprofile(request):
    user_account=request.user
    user_id=user_account.id
    print(user_account)
    print(user_id)
    
    return render(request ,'user/userprofile.html')

def aboutUs(request):
    return render(request ,'upevents/aboutus.html')

def editprofile(request):
    return render(request ,'user/editprofile.html')

def confirmeditprofile(request):
    return HttpResponse(' confirm edittt')

def submitpackage(request):
    if(request.method=='POST'):
        radio =request.POST.getlist['item_category[]']
        print(radio)
        # catpack=Package.objects.values('category')
        # cats=[item['category'] for item in catpack]
        # for cat in cats:
        #     print('product_%s'%cat)
        #     nameof='product_%s'%cat
        #     radio=request.POST.getlist[nameof]
        #     print(radio)
    #     for i in allcategory:
            
    #             radio=request.POST.get['product'+i]

    else:
        return HttpResponse("404-Not Found")
