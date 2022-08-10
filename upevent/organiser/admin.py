from django.contrib import admin


from organiser.form import EventAdmin,PackageAdmin,OrganiserAdmin,NewsAdmin,ContactAdmin

# Register your models here.
from .models import  Contact,News,Organiser,Event,Package


admin.site.register(Contact,ContactAdmin)
admin.site.register(News,NewsAdmin)
admin.site.register(Organiser,OrganiserAdmin)
admin.site.register(Event,EventAdmin)
admin.site.register(Package,PackageAdmin)
