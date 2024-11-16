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
    # food
    path("add/Shop/Food", views.add_food, name="add_food"),
    path("update/Shop/Food/<int:pk>", views.update_food, name="update_food"),
    path("delete/Shop/Food/<int:pk>", views.delete_food, name="delete_food"),
    # checkupDoctors
    path(
        "view/Checkup_details",
        views.CheckUpDetailsListView.as_view(),
        name="view_checkup_details",
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
    # checkupDoctors
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
    # Appointment for Checkup
    # all appointment in admin
    path("view/Appointment/Booking", views.view_appointment, name="view_appointment"),
    path("Appointment/Booking", views.booking_appointment, name="booking_appointment"),
    path(
        "Booking/ServiceOffered/<int:pk>",
        views.booking_service_offered,
        name="booking_service_offered",
    ),
    # path("update/Booking/Service Offered/<int:pk>", views.update_booking_service_offered, name="update_booking_service_offered"),
    # path("delete/Booking/Service Offered/<int:pk>", views.delete_booking_service_offered, name="delete_booking_service_offered"),
    path(
        "view/Booking/Service Offered",
        views.view_booking_service_offered,
        name="view_booking_service_offered",
    ),
    path(
        "Booking/Accessories/<int:pk>",
        views.booking_accessories,
        name="booking_accessories",
    ),
    # service token
    path(
        "token/add/Service Offered",
        views.add_token_service_offered,
        name="add_token_service_offered",
    ),
    path(
        "token/update/Service Offered/<int:pk>",
        views.update_token_service_offered,
        name="update_token_service_offered",
    ),
    path(
        "token/delete/Service Offered/<int:pk>",
        views.delete_token_service_offered,
        name="delete_token_service_offered",
    ),
    # path("token/view/Service Offered", views.view_token_service_offered, name="view_token_service_offered"),
    # path("Booking/Accessories/<int:pk>", views.booking_accessories, name="booking_accessories"),
    # path("Booking/Accessories/<int:pk>", views.booking_accessories, name="booking_accessories"),
    path("Booking/Food/<int:pk>", views.booking_food, name="booking_food"),
    # Checkup for user EDIT/DELETE
    path(
        "view/Booking/Appointment/",
        views.BookingAppointment.as_view(),
        name="user_booking_appointment",
    ),
    path(
        "edit/Appointment/Booking/<int:pk>",
        views.update_appointment,
        name="update_appointment",
    ),
    path(
        "delete/Appointment/Booking/<int:pk>",
        views.delete_appointment,
        name="delete_appointment",
    ),
    # checkup for admin Update
    path(
        "status/Appointment/Booking/<int:pk>",
        views.status_appointment,
        name="status_appointment",
    ),
]
