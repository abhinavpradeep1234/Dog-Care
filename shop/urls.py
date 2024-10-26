from django.urls import path
from . import views

urlpatterns = [
    path("view/Shop/Service", views.view_shop, name="view_shop"),
    path("add/Shop/Service", views.add_service, name="add_service"),
    path("update/Shop/Service/<int:pk>", views.update_service, name="update_service"),
    path("delete/Shop/Service/<int:pk>", views.delete_service, name="delete_service"),
    path("add/Shop/Accessories/", views.add_accessories, name="add_accessories"),
    path(
        "update/Shop/Accessories/<int:pk>",
        views.update_accessories,
        name="update_accessories",
    ),
    path(
        "delete/Shop/Accessories/<int:pk>",
        views.delete_accessories,
        name="delete_accessories",
    ),
    #food
    path("add/Shop/Food", views.add_food, name="add_food"),
    path("update/Shop/Food/<int:pk>", views.update_food, name="update_food"),
    path("delete/Shop/Food/<int:pk>", views.delete_food, name="delete_food"),
    #checkup
    path(
        "view/Checkup_details", views.view_checkup_details, name="view_checkup_details"
    ),
    path(
        "add/Doctors/Checkup_details",
        views.add_doctors_checkup_details,
        name="add_doctors_checkup_details",
    ),
    path(
        "update/Doctors/Checkup_details/<int:pk>",
        views.update_doctors_checkup_details,
        name="update_doctors_checkup_details",
    ),
    path(
        "delete/Doctors/Checkup_details/<int:pk>",
        views.delete_doctors_checkup_details,
        name="delete_doctors_checkup_details",
    ),
    path(
        "add/Token/Checkup_details",
        views.add_token_checkup_details,
        name="add_token_checkup_details",
    ),
    path(
        "update/Token/Checkup_details/<int:pk>",
        views.update_token_checkup_details,
        name="update_token_checkup_details",
    ),
    path(
        "delete/Token/Checkup_details/<int:pk>",
        views.delete_token_checkup_details,
        name="delete_token_checkup_details",
    ),
    #Appointment for Checkup
    path("view/Appointment/Booking", views.view_appointment, name="view_appointment"),
    path("Appointment/Booking", views.booking_appointment, name="booking_appointment"),
    
    
    
    # path("Book/Service Offered", views.add_service_offered, name="add_service_offered"),
    path("Booking/Accessories/<int:pk>", views.booking_accessories, name="booking_accessories"),
    # path("Booking/Food", views.booking_food, name="booking_food"),
]
