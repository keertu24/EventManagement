from django.contrib import admin

# Register your models here.
from .models import  Contact,News,Organiser


admin.site.register(Contact)
admin.site.register(News)
admin.site.register(Organiser)