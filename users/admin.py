from django.contrib import admin

# Register your models here.
from .models import CustomUser,Notification,Offers,Complaints

admin.site.register(CustomUser)
admin.site.register(Notification)
admin.site.register(Offers)
admin.site.register(Complaints)

