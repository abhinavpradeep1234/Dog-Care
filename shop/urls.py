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
        "view/checkup",
        views.DoctorsListView.as_view(),
        name="view_checkup_details",
    ),
    # page for admin view all tokens
    path(
        "view/Checkup/token",
        views.TokenListView.as_view(),
        name="view_tokens",
    ),
    # page for  admin view all service token
    path(
        "view/token/service",
        views.TokenServiceListView.as_view(),
        name="view_service_token",
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
    path(
        "view/Appointment/Booking",
        views.AppointmentListView.as_view(),
        name="view_appointment",
    ),
    path("Appointment/Booking", views.booking_appointment, name="booking_appointment"),
    # service booking Crud
    path(
        "Booking/ServiceOffered/<int:pk>",
        views.booking_service_offered,
        name="booking_service_offered",
    ),
    path(
        "update/Booking/Service Offered/<int:pk>",
        views.update_booking_service_offered,
        name="update_booking_service_offered",
    ),
    path(
        "delete/Booking/Service Offered/<int:pk>",
        views.delete_booking_service_offered,
        name="delete_booking_service_offered",
    ),
    # accessories booking CRUD
    path(
        "Booking/accessories/<int:pk>",
        views.booking_accessories,
        name="booking_accessories",
    ),
    path(
        "update/Booking/accessories/<int:pk>",
        views.update_booking_accessories,
        name="update_booking_accessories",
    ),
    path(
        "delete/Booking/accessories/<int:pk>",
        views.delete_booking_accessories,
        name="delete_booking_accessories",
    ),
    # food booking Crud
    path("Booking/Food/<int:pk>", views.booking_food, name="booking_food"),
    path(
        "update/Booking/Service Offered/<int:pk>",
        views.update_booking_food,
        name="update_booking_food",
    ),
    path(
        "delete/Booking/Service Offered/<int:pk>",
        views.delete_booking_food,
        name="delete_booking_food",
    ),
    # admin list for all booking
    path(
        "view/Booking/Service Offered",
        views.BookedServiceListView.as_view(),
        name="view_service_booking",
    ),
    path(
        "view/Booking/accessories",
        views.BookedAccessoriesListView.as_view(),
        name="view_accessories_booking",
    ),
    path(
        "view/Booking/food_products",
        views.BookedFoodListView.as_view(),
        name="view_food_booking",
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
    # Checkup for user EDIT/DELETE
    # path(
    #     "view/Booking/Appointment/",
    #     views.BookingAppointment.as_view(),
    #     name="user_booking_appointment",
    # ),
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
    # booking item in  dashboard food and accesories
    path("booking/service", views.BookedService.as_view(), name="booked_service"),
    path(
        "booking/accessories",
        views.BookedAccessories.as_view(),
        name="booked_accessories",
    ),
    path("booking/food", views.BookedFood.as_view(), name="booked_food"),
]
