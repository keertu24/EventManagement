from django.forms import ModelForm
from user.models import UserProfile,Order
from django.contrib import admin

class UserProfileForm(ModelForm):
    class Meta:
        model=UserProfile
        fields='__all__'

class UserProfileAdmin(admin.ModelAdmin):
    form=UserProfileForm
    list_display= ('user_name','user_mbl_no','user_dob','user_gender')

class OrderForm(ModelForm):
    class Meta:
        model=Order
        fields='__all__'

class OrderAdmin(admin.ModelAdmin):
    form=OrderForm
    list_display= ('order_id','user_name','name','mbl_no','email','date','time','est_people','venue','est_cost')