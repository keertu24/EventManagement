"""upevent URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index,name='index'),
   path('login/', views.userlogin, name='userLogin'),
   path('confirmlogin/', views.confirmlogin, name='userConfirmLogin'),
    path('signup/',views.signUp,name='userSignUp'),
    path('confirmsignup/',views.confirmsignUp,name='userconfirmSignUp'),
    path('logout/',views.confirmlogout,name='userlogout'),
    path('organiserlogin/', views.organiserlogin, name='organiserLogin'),
    path('forgotpass/',views.forgotpass,name='forgotpass'),
    path('otp/',views.otp,name='otp'),
    path('enterotp/',views.enterotp,name='enterotp'),
    path('confirmotp/',views.confirmotp,name='confirmotp'),
    path('repass/',views.repass,name='repass'),
    path('confirmrepass/',views.confirmrepass,name='confirmrepass'),
    path('organiserlogout/', views.organiserlogout, name='organiserLogout'),
    path("aboutus/",views.aboutUs,name='aboutus'),
    path("contactus/",views.contactUs,name='contactus'),
    path('newslist/',views.newslist,name='newslist'),
    path('news/<int:my_id>',views.newss,name='news'),
    path("organiser/",include("organiser.urls")),
    path("user/",include("user.urls")),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
