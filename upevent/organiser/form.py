from dataclasses import field
from pyexpat import model
import re

from django.forms import ModelForm
from organiser.models import News,Event,Package,Organiser,Contact
from django.core.exceptions import ValidationError
from django.contrib import admin
from django.contrib.auth.models import User


class EventForm(ModelForm):
    class Meta:
        model=Event
        fields='__all__'

class EventAdmin(admin.ModelAdmin):
    form=EventForm
    list_display= ('event_id','event_title')

class PackageForm(ModelForm):
    class Meta:
        model=Package
        fields='__all__'

class PackageAdmin(admin.ModelAdmin):
    form=PackageForm
    list_display= ('package_id','package_title','package_price')

class OrganiserForm(ModelForm):
    class Meta:
        model=Organiser
        fields='__all__'




class OrganiserAdmin(admin.ModelAdmin):
    form=OrganiserForm
    list_display= ('username','first_name','last_name','User_email','mobile_no')

class NewsForm(ModelForm):
    class Meta:
        model=News
        fields='__all__'

class NewsAdmin(admin.ModelAdmin):
    form=NewsForm
    list_display= ('news_id','news_title','pub_date')


class ContactForm(ModelForm):
    class Meta:
        model=Contact
        fields="__all__"

class ContactAdmin(admin.ModelAdmin):
    form=ContactForm
    list_display=('name','email','phone')




