from django.contrib import admin
from user.models import Cart,UserProfile,Order
from user.form import UserProfileAdmin,OrderAdmin
# Register your models here.
admin.site.register(Cart)
admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(Order,OrderAdmin)
