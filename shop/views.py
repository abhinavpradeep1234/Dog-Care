from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
from shop.models import (
    ServiceOffered,
    Accessories,
    DogFood,
    Doctors,
    Token,
    Appointment,
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
     BookingAccessories
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
        form = ServiceOfferedForm(request.POST, request.FILES)
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
    context = {"form": ServiceOfferedForm(), "page_title": "Add Service"}

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
# def booking_appointment(request):
#     if request.method == "POST":
#         form = BookingAppointmentForm(request.POST)
#         if form.is_valid():
#             appointment = form.save(commit=False)
#             appointment.username = request.user
#             appointment.save()
#             appointment.token_available = False
#             appointment.save()
#             messages.success(
#                 request,
#                 "Your Appointment Booking SuccessFully",
#                 extra_tags="alert-success",
#             )
#             return redirect("dashboard")
#         else:
#             for error_list in form.errors.values():
#                 for errors in error_list:
#                     messages.error(request, errors, extra_tags="alert-danger")
#     context = {"page_title": "Appointment Booking", "form": BookingAppointmentForm()}

#     return render(request, "add_update_service.html", context)
# def booking_appointment(request):
#     if request.method == "POST":
#         form = BookingAppointmentForm(request.POST)
#         if form.is_valid():
#             appointment = form.save(commit=False)
#             appointment.username = request.user
            
#             # Assuming the form has a field for the token
#             token = appointment.Token
            
#             # Check if the token is available
#             if token.token_available:
#                 appointment.save()
                
#                 # Update the token's availability
#                 token.token_available = False
#                 token.save()
                
#                 messages.success(
#                     request,
#                     "Your Appointment Booking Successful",
#                     extra_tags="alert-success",
#                 )
#                 return redirect("dashboard")
#             else:
#                 messages.error(request, "This token is no longer available.", extra_tags="alert-danger")
#         else:
#             for error_list in form.errors.values():
#                 for error in error_list:
#                     messages.error(request, error, extra_tags="alert-danger")
    
#     context = {
#         "page_title": "Appointment Booking", 
#         "form": BookingAppointmentForm()
#     }
#     return render(request, "add_update_service.html", context)


def view_appointment(request):
    context = {
        "page_title": "All Appointment",
        "appointments": Appointment.objects.all(),
    }
    return render(request, "view_appointment.html", context)





# def booking_appointment(request):
#     if request.method == "POST":
#         form = BookingAppointmentForm(request.POST)
#         if form.is_valid():
          
#             token = form.cleaned_data['Token']  # Ensure this is the field name for the token in your form
#             if token.not token_available:
#                 messages.error(request, "This token full", extra_tags="alert-danger")

                
              
#             # if token.token_available:  # Check if the token is available
#             appointment = form.save(commit=False)
#             appointment.username = request.user
#             appointment.save()
            
#             # Mark the token as unavailable
#             token.token_available = False
#             token.save()
            
#             messages.success(request, "Your Appointment Booking Successful", extra_tags="alert-success")
#             return redirect("dashboard")
#             # else:
#             #     messages.error(request, "This token is no longer available.", extra_tags="alert-danger")
#         else:
#             for error_list in form.errors.values():
#                 for error in error_list:
#                     messages.error(request, error, extra_tags="alert-danger")
    
#     context = {"page_title": "Appointment Booking", "form": BookingAppointmentForm()}
#     return render(request, "add_update_service.html", context)
#


#*****************************************
# def booking_appointment(request):
#     form = BookingAppointmentForm()

#     # Check if there are available tokens
#     available_tokens = Token.objects.filter(token_available=True)

#     if not available_tokens:
#         messages.error(request, "No tokens are currently available.", extra_tags="alert-danger")

#     if request.method == "POST":
#         form = BookingAppointmentForm(request.POST)
#         if form.is_valid():
#             token = form.cleaned_data['Token']


#             appointment = form.save(commit=False)
#             appointment.username = request.user
#             appointment.save()
            
#             # Mark the token as unavailable
#             token.token_available = False
#             token.save()
            
#             messages.success(request, "Your Appointment Booking Successful", extra_tags="alert-success")
#             return redirect("dashboard")

#         else:
#             # Handle form errors
#             for error_list in form.errors.values():
#                 for error in error_list:
#                     messages.error(request, error, extra_tags="alert-danger")
    
#     context = {"page_title": "Appointment Booking", "form": form}
#     return render(request, "add_update_service.html", context)





from datetime import timedelta
from django.utils import timezone
from django.contrib import messages
from django.shortcuts import redirect, render
from .models import Appointment, Token  # Make sure to import your models

def booking_appointment(request):
    today = timezone.localtime().date()
    form = BookingAppointmentForm()

    # Check if there are available tokens
    available_tokens = Token.objects.filter(token_available=True)

    if not available_tokens:
        messages.error(request, "No tokens are currentlydd available.", extra_tags="alert-danger")

    if request.method == "POST":
        form = BookingAppointmentForm(request.POST)
        if form.is_valid():
            token = form.cleaned_data['Token']
            appointment_date = form.cleaned_data['appointment_date']

            # Check if the selected token can be used for the given date
            if appointment_date >= today and appointment_date <= (today + timedelta(days=2)):
                appointment = form.save(commit=False)
                appointment.username = request.user
                appointment.save()
                
                # Mark the token as unavailable for that specific day
                token.token_available = False
                token.save()
                
                messages.success(request, "Your Appointment Booking Successful", extra_tags="alert-success")
                return redirect("dashboard")
            else:
                messages.error(request, "You can only book this token for today or the next two days.", extra_tags="alert-danger")
        else:
            # Handle form errors
            for error_list in form.errors.values():
                for error in error_list:
                    messages.error(request, error, extra_tags="alert-danger")

    context = {"page_title": "Appointment Booking", "form": form}
    return render(request, "add_update_service.html", context)

#####booking #####


# def add_service_offered(request):
#     if request.method == "POST":
#         form = BookServiceOfferedForm(request.POST)
#         if form.is_valid():
#             booking = form.save(commit=False)
#             booking.username = request.user
#             booking.email = request.user
#             booking.save()
#             messages.success(
#                 request,
#                 "Your Booking Successfully, Delivery Expected Two Days",
#                 extra_tags="alert-success",
#             )
#             return redirect("dashboard")

#         else:
#             for error_list in form.errors.values():
#                 for errors in error_list:
#                     messages.error(request, errors, extra_tags="alert-danger")

#     context = {"page_title": "BooK Now", "form": BookServiceOfferedForm()}
#     return render(request, "booking_dog_care.html", context)


# def booking_accessories(request):
#     if request.method == "POST":
#         form = BookAccessoriesForm(request.POST)
#         if form.is_valid():
#             books = form.save(commit=False)
#             books.username = request.user
#             books.email = request.user
#             a=int(books.quantity)
#             b=int(books.total_stock)
#                         # Check if requested quantity exceeds available stock
#             if a > b:
#                 messages.error(
#                     request,
#                     "Out of stock! The quantity must be less than or equal to the available stock.",
#                     extra_tags="alert-danger",
#                 )
#             else:
#                 # Update total stock after booking
#                 books.total_stock -= books.quantity

#             # if books.quantity > books.total_stock:
#             #     messages.error(request,"Out of stock the quantity mus t be less than taht of total stock",extra_tags="alert-danger")


#                 books.save()
#                 messages.success(
#                     request,
#                     "Your booking successfully Delivery Expected 2 Days ",
#                     extra_tags="alert-danger",
#                 )
#                 return redirect("dashboard")
#         else:
#             for error_list in form.errors.values():
#                 for errors in error_list:
#                     messages.error(request, errors, extra_tags="alert-danger")
#     context = {"page_title": "Book Now", "form": BookAccessoriesForm()}
#     return render(request, "booking_dog_care.html", context)


# def booking_accessories(request,pk):
#     all_accessorie=get_object_or_404(Accessories,id=pk)

#     if request.method == "POST":
#         form = BookAccessoriesForm(request.POST)
#         if form.is_valid():
#             books = form.save(commit=False)
#             books.username = request.user
#             books.email = request.user.email  # Assuming you want the user's email

#             # Fetch the related accessory's total stock
#             accessory = books.accessories_name  # Access the Accessories object
#             total_stock = accessory.total_stock  # Get the total_stock from Accessories

#             # Check if requested quantity exceeds available stock
#             if books.quantity > total_stock:
#                 messages.error(
#                     request,
#                     "Out of stock!",
#                     extra_tags="alert-danger",
#                 )
#             else:
#                 # Update total stock after booking
#                 accessory.total_stock -= books.quantity
#                 accessory.save()  # Save the updated total stock

#                 # Save the booking
#                 books.save()

#                 # Success message
#                 messages.success(
#                     request,
#                     "Your booking was successful! Delivery expected in 2 days.",
#                     extra_tags="alert-success",
#                 )
#                 return redirect("dashboard")
#         else:
#             # Handle form errors
#             for error_list in form.errors.values():
#                 for errors in error_list:
#                     messages.error(request, errors, extra_tags="alert-danger")

#     # Display form on GET request
#     context = {"page_title": "Book Now", "form": BookAccessoriesForm(),"all_accessorie":all_accessorie}
#     return render(request, "booking_dog_care.html", context)


def booking_accessories(request, pk):
    # Fetch the selected accessory by its primary key (pk)
    all_accessorie = get_object_or_404(Accessories, id=pk)

    if request.method == "POST":
        form = BookAccessoriesForm(request.POST)
        
        if form.is_valid():
            # Handle the valid form submission
            books = form.save(commit=False)
            books.username = request.user
            books.email = request.user.email
            books.accessories_name = all_accessorie

            if books.quantity > all_accessorie.total_stock:
                messages.error(request, "Out of stock!", extra_tags="alert-danger")
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
        # Pre-fill form with initial data
        initial_data = {
            'accessories_name': all_accessorie,  # Pre-fill accessories_name
            'price': all_accessorie.price,  # Pre-fill price
        }

        # Debugging: Print initial data
        print(f"Initial data passed to the form: {initial_data}")

        form = BookAccessoriesForm(initial=initial_data)

    # Render the booking page with both the form and accessory details
    context = {
        "page_title": "Book Now",
        "form": form,
        "all_accessorie": all_accessorie,
    }
    return render(request, "booking_dog_care.html", context)


# def book_food(request):
#     if request.method == "POST":
#         form = BookFoodForm(request.POST)
#         if form.is_valid():
#             books = form.save(commit=False)
#             books.username = request.user
#             books.email = request.user
#             books.save()

#             messages.success(
#                 request,
#                 "Your booking successfully Delivery Expected 2 Days ",
#                 extra_tags="alert-danger",
#             )
#             return redirect("dashboard")
#         else:
#             for error_list in form.errors.values():
#                 for errors in error_list:
#                     messages.error(request, errors, extra_tags="alert-danger")
#     context = {"page_title": "Book Now", "form": BookFoodForm()}
#     return render(request, "booking_dog_care.html", context)
