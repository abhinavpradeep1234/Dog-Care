from django.contrib import admin

# Register your models here.
from shop.models import ServiceOffered,Accessories, DogFood,Doctors,Token,Appointment

admin.site.register(ServiceOffered)
admin.site.register(Accessories)
admin.site.register(DogFood)
admin.site.register(Doctors)
admin.site.register(Token)
admin.site.register(Appointment)
