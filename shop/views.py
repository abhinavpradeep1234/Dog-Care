from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import timedelta
from django.utils import timezone

# Create your views here.
from shop.models import (
    ServiceOffered,
    Accessories,
    DogFood,
    Doctors,
    Token,
    Appointment,
    BookingService,
    BookingAccessories,
    BookingFood,
    TokenService,
)

from shop.forms import (
    BookServiceOfferedForm,
    BookAccessoriesForm,
    BookFoodForm,
    ServiceOfferedForm,
    AccessoriesForm,
    DogFoodForm,
    DoctorsForm,
    TokenForm,
    BookingAppointmentForm,
    ServiceTokenForm,
)

from django.shortcuts import get_object_or_404


def view_shop(request):
    context = {
        "page_title": "Doggy Essentials",
        "all_services": ServiceOffered.objects.all(),
        "all_accessories": Accessories.objects.all(),
        "all_foods": DogFood.objects.all(),
    }
    return render(request, "view_service_offerd.html", context)


# Service CRUD


def add_service(request):
    if request.method == "POST":
        form = ServiceOfferedForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Service Added Successfully", extra_tags="alert-success"
            )
            return redirect("shop_dashboard")
        else:
            for error_list in form.errors.values():
                for errors in error_list:
                    messages.error(request, errors, extra_tags="alert-danger")
    context = {"form": ServiceOfferedForm(), "page_title": "Add Service", "stock": True}

    return render(request, "add_update_service.html", context)


def update_service(request, pk):
    to_update = get_object_or_404(ServiceOffered, id=pk)
    if request.method == "POST":

        form = ServiceOfferedForm(request.POST, request.FILES, instance=to_update)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Service Updated Successfully", extra_tags="alert-success"
            )
            return redirect("shop_dashboard")
        else:
            for error_list in form.errors.values():
                for errors in error_list:
                    messages.error(request, errors, extra_tags="alert-danger")
    context = {
        "form": ServiceOfferedForm(instance=to_update),
        "page_title": "Update Service",
    }

    return render(request, "add_update_service.html", context)


def delete_service(request, pk):
    to_delete = get_object_or_404(ServiceOffered, id=pk)
    to_delete.delete()
    messages.success(
        request, "Service Deleted SUccessfully", extra_tags="alert-success"
    )
    return redirect("shop_dashboard")


# Accessories CRUD
def add_accessories(request):
    if request.method == "POST":
        form = AccessoriesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Accessories Added Successfully", extra_tags="alert-success"
            )
            return redirect("shop_dashboard")
        else:
            for error_list in form.errors.values():
                for errors in error_list:
                    messages.error(request, errors, extra_tags="alert-danger")
    context = {
        "page_title": "Add Accessories",
        "form": AccessoriesForm(),
        "total_stock": Accessories.objects.all(),
    }
    return render(request, "add_update_service.html", context)


def update_accessories(request, pk):
    to_update = get_object_or_404(Accessories, id=pk)
    if request.method == "POST":
        form = AccessoriesForm(request.POST, request.FILES, instance=to_update)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Accessories Updated Successfully", extra_tags="alert-success"
            )
            return redirect("shop_dashboard")
        else:
            for error_list in form.errors.values():
                for errors in error_list:
                    messages.error(request, errors, extra_tags="alert-danger")
    context = {
        "page_title": "Update Accessories",
        "form": AccessoriesForm(instance=to_update),
    }

    return render(request, "add_update_service.html", context)


def delete_accessories(request, pk):
    to_delete = get_object_or_404(Accessories, id=pk)
    to_delete.delete()
    messages.success(
        request, "Accesories Deleted Successfully", extra_tags="alert-success"
    )
    return redirect("shop_dashboard")


### Dog Food CRUD


def add_food(request):
    if request.method == "POST":
        form = DogFoodForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Food Products Added Successfully", extra_tags="alert-success"
            )
            return redirect("shop_dashboard")
        else:
            for error_list in form.errors.values():
                for errors in error_list:
                    messages.error(request, errors, extra_tags="alert-danger")
    context = {"page_title": "Add Food Products", "form": DogFoodForm()}
    return render(request, "add_update_service.html", context)


def update_food(request, pk):
    to_update = get_object_or_404(DogFood, id=pk)
    if request.method == "POST":
        form = DogFoodForm(request.POST, request.FILES, instance=to_update)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Food Products Updated Successfully",
                extra_tags="alert-success",
            )
            return redirect("shop_dashboard")
        else:
            for error_list in form.errors.values():
                for errors in error_list:
                    messages.error(request, errors, extra_tags="alert-danger")
    context = {
        "page_title": "Update Food Products",
        "form": DogFoodForm(instance=to_update),
    }
    return render(request, "add_update_service.html", context)


def delete_food(request, pk):
    to_update = get_object_or_404(DogFood, id=pk)
    to_update.delete()
    messages.success(
        request, " Food Item Deleted SuccessFully", extra_tags="alert-success"
    )
    return redirect("shop_dashboard")


#  Doctor/Token CRUD


def view_checkup_details(request):
    context = {
        "page_title": "View Checkup Details",
        "all_doctors": Doctors.objects.all(),
        "all_tokens": Token.objects.all(),
        "all_tokens_services": TokenService.objects.all(),
    }
    return render(request, "view_checkup_doctors_tokens.html", context)


def add_doctors_checkup_details(request):
    if request.method == "POST":
        form = DoctorsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Doctors Details Added Successfully",
                extra_tags="alert-success",
            )
            return redirect("shop_dashboard")
        else:
            for error_list in form.errors.values():
                for errors in error_list:
                    messages.error(request, errors, extra_tags="alert-danger")

    context = {"page_title": "Add Doctors Details", "form": DoctorsForm()}
    return render(request, "add_update_service.html", context)


def update_doctors_checkup_details(request, pk):
    to_update = get_object_or_404(Doctors, id=pk)
    if request.method == "POST":
        form = DoctorsForm(request.POST, instance=to_update)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Doctors Details Updated Successfully",
                extra_tags="alert-success",
            )
            return redirect("shop_dashboard")
        else:
            for error_list in form.errors.values():
                for errors in error_list:
                    messages.error(request, errors, extra_tags="alert-danger")

    context = {
        "page_title": "Update Doctors Details",
        "form": DoctorsForm(instance=to_update),
    }
    return render(request, "add_update_service.html", context)


def delete_doctors_checkup_details(request, pk):
    to_delete = get_object_or_404(Doctors, id=pk)
    to_delete.delete()
    messages.success(
        request, "Doctors Deleted SuccessFully", extra_tags="alert-success"
    )
    return redirect("shop_dashboard")


#
def add_token_checkup_details(request):
    if request.method == "POST":
        form = TokenForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Token Added Successfully",
                extra_tags="alert-success",
            )
            return redirect("shop_dashboard")
        else:
            for error_list in form.errors.values():
                for errors in error_list:
                    messages.error(request, errors, extra_tags="alert-danger")

    context = {"page_title": "Add Token Details", "form": TokenForm()}
    return render(request, "add_update_service.html", context)


def update_token_checkup_details(request, pk):
    to_update = get_object_or_404(Token, id=pk)
    if request.method == "POST":
        form = TokenForm(request.POST, instance=to_update)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Token Updated Successfully",
                extra_tags="alert-success",
            )
            return redirect("shop_dashboard")
        else:
            for error_list in form.errors.values():
                for errors in error_list:
                    messages.error(request, errors, extra_tags="alert-danger")

    context = {
        "page_title": "Update Token Details",
        "form": TokenForm(instance=to_update),
    }
    return render(request, "add_update_service.html", context)


def delete_token_checkup_details(request, pk):
    to_delete = get_object_or_404(Token, id=pk)
    to_delete.delete()
    messages.success(request, "Token Deleted SuccessFully", extra_tags="alert-success")
    return redirect("shop_dashboard")


# appointment


def view_appointment(request):
    context = {
        "page_title": "All Appointment",
        "appointments": Appointment.objects.all(),
    }
    return render(request, "view_appointment.html", context)








from django.utils import timezone
from datetime import timedelta
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Token, TokenAvailability, Appointment
from shop.forms import BookingAppointmentForm

def booking_appointment(request):
    today = timezone.localtime().date()
    form = BookingAppointmentForm()

    if request.method == "POST":
        form = BookingAppointmentForm(request.POST)
        if form.is_valid():
            token = form.cleaned_data["Token"]
            appointment_date = form.cleaned_data["appointment_date"]

            # Check if the selected date is within the allowed range (today or next two days)
            if today <= appointment_date <= (today + timedelta(days=2)):
                # Get or create a TokenAvailability entry for the selected date
                token_availability, created = TokenAvailability.objects.get_or_create(
                    token=token, date=appointment_date
                )

                if token_availability.is_available:
                    # Save the appointment
                    appointment = form.save(commit=False)
                    appointment.username = request.user
                    appointment.save()

                    # Mark the token as unavailable for the selected date
                    token_availability.is_available = False
                    token_availability.save()

                    messages.success(
                        request,
                        "Your Appointment Booking was Successful",
                        extra_tags="alert-success",
                    )
                    return redirect("dashboard")
                else:
                    messages.error(
                        request,
                        "This token is not available for the selected date.",
                        extra_tags="alert-danger",
                    )
            else:
                messages.error(
                    request,
                    "You can only book this token for today or the next two days.",
                    extra_tags="alert-danger",
                )
        else:
            for error_list in form.errors.values():
                for error in error_list:
                    messages.error(request, error, extra_tags="alert-danger")

    # Display all tokens regardless of general `token_available` field, as we're managing availability by date
    available_tokens = Token.objects.all()

    context = {"page_title": "Appointment Booking", "form": form, "available_tokens": available_tokens}
    return render(request, "add_update_service.html", context)


# def booking_appointment(request):
#     today = timezone.localtime().date()
#     form = BookingAppointmentForm()

#     # Check if there are available tokens
#     available_tokens = Token.objects.filter(token_available=True)

#     if not available_tokens:
#         messages.error(
#             request, "No tokens are currentlydd available.", extra_tags="alert-danger"
#         )

#     if request.method == "POST":
#         form = BookingAppointmentForm(request.POST)
#         if form.is_valid():
#             token = form.cleaned_data["Token"]
#             appointment_date = form.cleaned_data["appointment_date"]

#             # Check if the selected token can be used for the given date
#             if appointment_date >= today and appointment_date <= (
#                 today + timedelta(days=2)
#             ):
#                 appointment = form.save(commit=False)
#                 appointment.username = request.user
#                 appointment.save()

#                 # Mark the token as unavailable for that specific day
#                 token.token_available = False
#                 token.save()

#                 messages.success(
#                     request,
#                     "Your Appointment Booking Successful",
#                     extra_tags="alert-success",
#                 )
#                 return redirect("dashboard")
#             else:
#                 messages.error(
#                     request,
#                     "You can only book this token for today or the next two days.",
#                     extra_tags="alert-danger",
#                 )
#         else:

#             for error_list in form.errors.values():
#                 for error in error_list:
#                     messages.error(request, error, extra_tags="alert-danger")

#     context = {"page_title": "Appointment Booking", "form": form}
#     return render(request, "add_update_service.html", context)


#####Booking Doggy Essential #####


def booking_service_offered(request, pk):
    all_service = get_object_or_404(ServiceOffered, id=pk)
    token = TokenService.objects.filter(available=True)
    if not token:
        messages.error(
            request, "Sorry Booking Slot is currently Full", extra_tags="alert-danger"
        )

    if request.method == "POST":
        form = BookServiceOfferedForm(request.POST)
        if form.is_valid():
            selected_token = form.cleaned_data["token"]

            booking_service = form.save(commit=False)
            booking_service.username = request.user
            booking_service.email = request.user
            booking_service.save()
            selected_token.available = False
            selected_token.save()
            messages.success(
                request,
                "Your Booking Successfully, Delivery Expected Two Days",
                extra_tags="alert-success",
            )
            return redirect("dashboard")

        else:
            for error_list in form.errors.values():
                for errors in error_list:
                    messages.error(request, errors, extra_tags="alert-danger")

    initial_data = {"service_name": all_service, "price": all_service.price}

    form = BookServiceOfferedForm(initial=initial_data)
    context = {
        "page_title": "Service Booking",
        "form": form,
        "all_service": all_service,
    }

    return render(request, "add_update_service.html", context)


def booking_accessories(request, pk):
    all_accessorie = get_object_or_404(Accessories, id=pk)
    print("Request me.thod:", request.method)  

    if request.method == "POST":
        print("POST request received")  
        form = BookAccessoriesForm(request.POST)

        if form.is_valid():
            print("Form is valid")
            books = form.save(commit=False)
            books.username = request.user
            books.email = request.user.email
            books.accessories_name = all_accessorie

            if books.quantity > all_accessorie.total_stock:
                messages.error(request, "Out of Stock!!", extra_tags="alert-danger")
            elif all_accessorie.total_stock == 0:
                messages.error(request, "Out of Stock!", extra_tags="alert-danger")

            else:
                

                all_accessorie.total_stock -= books.quantity

                all_accessorie.save()
                books.save()
                messages.success(
                    request,
                    "Your booking was successful! Delivery expected in 2 days.",
                    extra_tags="alert-success",
                )
                return redirect("dashboard")
    else:

        initial_data = {
            "accessories_name": all_accessorie,  # Pre-fill accessories_name
            "price": all_accessorie.price,  # Pre-fill price
        }

        form = BookAccessoriesForm(initial=initial_data)

    context = {
        "page_title": "Book Now",
        "form": form,
        "all_accessorie": all_accessorie,
        "stock": True,
    }
    return render(request, "booking_dog_care.html", context)


def booking_food(request, pk):
    all_food = get_object_or_404(DogFood, id=pk)

    if request.method == "POST":
        form = BookFoodForm(request.POST)
        if form.is_valid():

            books = form.save(commit=False)
            books.username = request.user
            books.email = request.user

            if books.quantity > all_food.total_stock:
                messages.error(request, "Out of Stock!!", extra_tags="alert-danger")

            elif all_food.total_stock == 0:
                messages.error(request, "Out of Stock!!", extra_tags="alert-danger")

            else:
                all_food.total_stock -= books.quantity
                all_food.save()
                books.save()

                messages.success(
                    request,
                    "Your booking successfully Delivery Expected 2 Days ",
                    extra_tags="alert-success",
                )
                return redirect("dashboard")
        else:
            for error_list in form.errors.values():
                for errors in error_list:
                    messages.error(request, errors, extra_tags="alert-danger")
    initial_data = {"Food_name": all_food, "price": all_food.price}
    form = BookFoodForm(initial=initial_data)
    context = {
        "page_title": "Book Now",
        "form": form,
        "stock": True,
        "all_food": all_food,
    }
    return render(request, "add_update_service.html", context)


def view_booking_service_offered(request):
    context = {
        "page_title": " All Service Booking",
        "all_users": BookingService.objects.all(),
        "all_accessories": BookingAccessories.objects.all(),
        "all_foods": BookingFood.objects.all(),
    }
    return render(request, "view_service_booking.html", context)


def add_token_service_offered(request):
    if request.method == "POST":
        form = ServiceTokenForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Service Token Added SuccessFully", extra_tags="alert-success"
            )
            return redirect("shop_dashboard")

    # else:
    #     for error_list in form.errors.values():
    #         for errors in error_list:
    #             messages.error(request,errors,extra_tags="alert-danger")
    context = {"page_title": "Add Token", "form": ServiceTokenForm}
    return render(request, "add_update_service.html", context)


def update_token_service_offered(request, pk):
    to_update = get_object_or_404(TokenService, id=pk)
    if request.method == "POST":
        form = ServiceTokenForm(request.POST, instance=to_update)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Service Token Updated SuccessFully",
                extra_tags="alert-success",
            )
            return redirect("shop_dashboard")

    # else:
    # for error_list in form.errors.values():
    #     for errors in error_list:
    #         messages.error(request, errors, extra_tags="alert-danger")
    context = {"page_title": "Add Token", "form": ServiceTokenForm(instance=to_update)}
    return render(request, "add_update_service.html", context)


def delete_token_service_offered(request, pk):
    to_delete = get_object_or_404(TokenService, id=pk)
    to_delete.delete()
    messages.success(
        request, "Service Token Added SuccessFully", extra_tags="alert-success"
    )
    return redirect("shop_dashboard")


# def view_token_service_offered(request):
#     context={"all_tokens":TokenService.objects.all()}
#     return render (request,"view_checkup_doctors_tokens.html",context)
