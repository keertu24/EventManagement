import re
from tempfile import template
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,  login, logout
from organiser.models import Contact,News,Organiser,Event


# Create your views here.
def index(request):
    events=Event.objects.all()

    return render(request,'upevents/index.html',{'events':events})

def userlogin(request):
    # user login page
    return render(request,'upevents/userlogin.html')

def confirmlogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpass']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request,user)
            messages.success(request, "Successfully Logged In")
            return redirect("/user")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("/user")

    return HttpResponse("404- Not found")
    #it will confirm that is authecate user

def signUp(request):
    #Just template to show the signup page
   return render(request,'upevents/usersignup.html')


def confirmsignUp(request):
    #end point to add a user
    try:
        print(request)
        if request.method=='POST':
            username=request.POST['signupusername']
            fname =request.POST['signupfname']
            lname=request.POST['signuplname']
            mblno=request.POST['signupmblno']
            email=request.POST['signupemail']
            password=request.POST['signuppassword']
            conpassword=request.POST['signupconfirmpassword']

        #checking errors
            if len(username)>10:
                messages.error(request, " Your user name must be under 10 characters")
                return redirect('/signup')

            if not username.isalnum():
                messages.error(request, " User name should only contain letters and numbers")
                return redirect('/signup')

            if (password!= conpassword):
                messages.error(request, " Passwords do not match")
                return redirect('/signup')
            

        # put this things in try block 
            #create the user
            myuser=User.objects.create_user(username,email,password)
            myuser.first_name=fname
            myuser.last_name=lname
        # myuser.mblno=mblno
            myuser.save()
            messages.success(request,"success")
            return redirect('/signup')
        else:
                return HttpResponse("404- Not found")
    except Exception as e:
        messages.error(request, "Enter details properly, Username must be unique")
        return redirect('/signup') 


def confirmlogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/user')

def aboutUs(request):
    return render (request,'upevents/about.html')

def contactUs(request):
    if request.method=="POST":
        print(request)
        name=request.POST.get('contactname', '')
        email=request.POST.get('contactemail', '')
        phone=request.POST.get('contactphone', '')
        desc=request.POST.get('contactdesc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, "upevents/contactus.html")

def newslist(request):
    news_obj=News.objects.all
    #to display news and inform about the organisation 
    return render(request,'upevents/newslist.html',{'news_obj':news_obj})

def newss(request,my_id):
    # fetch the product using id 
    # to display news and inform about the organisation 
    news_content=News.objects.filter(news_id=my_id)
   
    return render(request,'upevents/news.html',{'news_content':news_content})


def organiserlogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['orgusername']
        loginpassword=request.POST['orgpassword']
        user_object=Organiser.objects.filter(username=loginusername)
        pass_object=Organiser.objects.filter(password=loginpassword)
        # creating list for username and password 
        user_list=[]
        pass_list=[]
        
        for i in range(len(user_object)):
            user_list.append(user_object[i])

        for i in range(len(pass_object)):
            pass_list.append(pass_object[i])
     
        if not user_list:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("/")

        if not pass_list:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("/")
        #  checking whether both list elements are same are not 
        if(user_list==pass_list):
            user=authenticate(username= loginusername, password= loginpassword)
            if user is not None:
                login(request,user)
                messages.success(request, "Successfully Logged In")
                return redirect("/organiser")
            else:
                messages.error(request, "Invalid credentials! Please try again")
                return redirect("/")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("/")

    return HttpResponse("404- Not found")

def organiserlogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/')