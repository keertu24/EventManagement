from django.contrib import admin
from user.models import Cart,UserProfile,Order

# Register your models here.
admin.site.register(Cart)
admin.site.register(UserProfile)
admin.site.register(Order)
