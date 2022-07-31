from django.contrib import admin

# Register your models here.
from .models import  Contact,News,Organiser,Service,Event,Package


admin.site.register(Contact)
admin.site.register(News)
admin.site.register(Organiser)
admin.site.register(Service)
admin.site.register(Event)
admin.site.register(Package)