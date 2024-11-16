from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import timedelta
from django.utils import timezone
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.core.exceptions import ValidationError
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
    AppointmentStatusForm,
)

from django.shortcuts import get_object_or_404


@login_required(login_url="signup")
def view_shop(request):
    context = {
        "page_title": "Doggy Essentials",
        "all_services": ServiceOffered.objects.all(),
        "all_accessories": Accessories.objects.all(),
        "all_foods": DogFood.objects.all(),
    }
    return render(request, "view_doggie_essential.html", context)


# Service CRUD


@login_required(login_url="signup")
def add_service(request):
    if request.user.role == "SHOP OWNER":
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
        context = {
            "form": ServiceOfferedForm(),
            "page_title": "Add Service",
            "stock": True,
        }

        return render(request, "add_update.html", context)
    return redirect("403")


@login_required(login_url="signup")
def update_service(request, pk):
    if request.user.role == "SHOP OWNER":

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

        return render(request, "add_update.html", context)
    return redirect("403")


@login_required(login_url="signup")
def delete_service(request, pk):
    if request.user.role == "SHOP OWNER":
        to_delete = get_object_or_404(ServiceOffered, id=pk)
        to_delete.delete()
        messages.success(
            request, "Service Deleted SUccessfully", extra_tags="alert-success"
        )
        return redirect("shop_dashboard")
    return redirect("403")


# Accessories CRUD
@login_required(login_url="signup")
def add_accessories(request):
    if request.user.role == "SHOP OWNER":
        if request.method == "POST":
            form = AccessoriesForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(
                    request,
                    "Accessories Added Successfully",
                    extra_tags="alert-success",
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
        return render(request, "add_update.html", context)
    return redirect("403")


@login_required(login_url="signup")
def update_accessories(request, pk):
    if request.user.role == "SHOP OWNER":
        to_update = get_object_or_404(Accessories, id=pk)
        if request.method == "POST":
            form = AccessoriesForm(request.POST, request.FILES, instance=to_update)
            if form.is_valid():
                form.save()
                messages.success(
                    request,
                    "Accessories Updated Successfully",
                    extra_tags="alert-success",
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

        return render(request, "add_update.html", context)
    return redirect("403")


@login_required(login_url="signup")
def delete_accessories(request, pk):
    if request.user.role == "SHOP OWNER":
        to_delete = get_object_or_404(Accessories, id=pk)
        to_delete.delete()
        messages.success(
            request, "Accesories Deleted Successfully", extra_tags="alert-success"
        )
        return redirect("shop_dashboard")
    return redirect("403")


### Dog Food CRUD


@login_required(login_url="signup")
def add_food(request):
    if request.user.role == "SHOP OWNER":
        if request.method == "POST":
            form = DogFoodForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(
                    request,
                    "Food Products Added Successfully",
                    extra_tags="alert-success",
                )
                return redirect("shop_dashboard")
            else:
                for error_list in form.errors.values():
                    for errors in error_list:
                        messages.error(request, errors, extra_tags="alert-danger")
        context = {"page_title": "Add Food Products", "form": DogFoodForm()}
        return render(request, "add_update.html", context)
    return redirect("403")


@login_required(login_url="signup")
def update_food(request, pk):
    if request.user.role == "SHOP OWNER":

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
        return render(request, "add_update.html", context)
    return redirect("403")


@login_required(login_url="signup")
def delete_food(request, pk):
    if request.user.role == "SHOP OWNER":

        to_update = get_object_or_404(DogFood, id=pk)
        to_update.delete()
        messages.success(
            request, " Food Item Deleted SuccessFully", extra_tags="alert-success"
        )
        return redirect("shop_dashboard")
    return redirect("403")


# services Token CRUD
@login_required(login_url="signup")
def add_token_service_offered(request):
    if request.user.role == "SHOP OWNER":

        if request.method == "POST":
            form = ServiceTokenForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(
                    request,
                    "Service Token Added SuccessFully",
                    extra_tags="alert-success",
                )
                return redirect("shop_dashboard")
            else:

                for error_list in form.errors.values():
                    for errors in error_list:
                        messages.error(request, errors, extra_tags="alert-danger")

        context = {"page_title": "Add Token", "form": ServiceTokenForm}
        return render(request, "add_update.html", context)
    return redirect("403")


@login_required(login_url="signup")
def update_token_service_offered(request, pk):
    if request.user.role == "SHOP OWNER":

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
            else:
                for error_list in form.errors.values():
                    for errors in error_list:
                        messages.error(request, errors, extra_tags="alert-danger")

        context = {
            "page_title": "Add Token",
            "form": ServiceTokenForm(instance=to_update),
        }
        return render(request, "add_update.html", context)
    return redirect("403")


@login_required(login_url="signup")
def delete_token_service_offered(request, pk):
    if request.user.role == "SHOP OWNER":

        to_delete = get_object_or_404(TokenService, id=pk)
        to_delete.delete()
        messages.success(
            request, "Service Token Added SuccessFully", extra_tags="alert-success"
        )
        return redirect("shop_dashboard")
    return redirect("403")


# Booking Doggies Essential
@login_required(login_url="signup")
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
            booking_service.service_name = all_service
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

    return render(request, "add_update.html", context)


@login_required(login_url="signup")
def booking_accessories(request, pk):
    all_accessorie = get_object_or_404(Accessories, id=pk)

    if request.method == "POST":

        form = BookAccessoriesForm(request.POST)

        if form.is_valid():
            try:
                books = form.save(commit=False)
                books.username = request.user
                books.email = request.user.email
                books.accessories_name = all_accessorie

                if books.quantity > all_accessorie.total_stock:
                    messages.error(
                        request,
                        "Not enough stock available.",
                        extra_tags="alert-danger",
                    )

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
            except ValidationError as e:
                messages.error(request, f"{e}", extra_tags="alert-danger")

    else:

        initial_data = {
            "accessories_name": all_accessorie,
            "price": all_accessorie.price,
        }

        form = BookAccessoriesForm(initial=initial_data)

    context = {
        "page_title": "Book Now",
        "form": form,
        "all_accessorie": all_accessorie,
        "stock": True,
        "accessories": True,
    }
    return render(request, "booking_dog_care.html", context)


@login_required(login_url="signup")
def booking_food(request, pk):
    all_food = get_object_or_404(DogFood, id=pk)
    if request.method == "POST":
        form = BookFoodForm(request.POST)
        if form.is_valid():
            try:
                booking = form.save(commit=False)
                booking.username = request.user
                booking.Food_name = all_food

                if booking.quantity > all_food.total_stock:
                    messages.error(
                        request,
                        "Not enough stock available.",
                        extra_tags="alert-danger",
                    )

                else:
                    all_food.total_stock -= booking.quantity
                    all_food.save()

                    booking.save()
                    messages.success(
                        request,
                        "Booking Successfully Delivery Expected 2 Days",
                        extra_tags="alert-success",
                    )

                    return redirect("shop_dashboard")

            except ValidationError as e:
                messages.error(request, f"{e}", extra_tags="alert-danger")

        else:
            for error_list in form.errors.values():
                for errors in error_list:
                    messages.error(request, errors, extra_tags="alert-danger")

    initial_data = {"Food_name": all_food, "price": all_food.price}
    form = BookFoodForm(initial=initial_data)
    context = {
        "form": form,
        "page_title": "Food Product Booking",
        "all_food": all_food,
        "food": True,
    }

    return render(request, "booking_dog_care.html", context)


@login_required(login_url="signup")
def view_booking_service_offered(request):
    context = {
        "page_title": " All Service Booking",
        "all_users": BookingService.objects.all(),
        "all_accessories": BookingAccessories.objects.all(),
        "all_foods": BookingFood.objects.all(),
    }
    return render(request, "view_service_booking.html", context)


#  Doctor/Token CRUD


class CheckUpDetailsListView(ListView):
    template_name = "view_checkup_doctors_tokens.html"
    context_object_name = "all_doctors"
    paginate_by = 4

    # Custom queryset if you want more control over the data displayed
    def get_queryset(self):
        return Doctors.objects.all()  # Custom queryset (e.g., you could add filters)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "View Checkup Details"
        context["all_tokens"] = Token.objects.all()
        context["all_tokens_services"] = TokenService.objects.all()
        return context


# class CheckUpDetailsListView(ListView):
#     template_name="view_checkup_doctors_tokens.html"
#     paginate_by=4
#     ordering=['id']
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["all_doctors"] = "View Checkup Details"
#         context["page_title"] = Doctors.objects.all(),
#         context["all_tokens"] = Token.objects.all(),
#         context["all_tokens_services"] = TokenService.objects.all(),
#         return context

# def view_checkup_details(request):
#     context = {
#         "page_title": "View Checkup Details",
#         "all_doctors": Doctors.objects.all(),
#         "all_tokens": Token.objects.all(),
#         "all_tokens_services": TokenService.objects.all(),
#     }
#     return render(request, "view_checkup_doctors_tokens.html", context)


@login_required(login_url="signup")
def add_doctors_checkup_details(request):
    if request.user.role == "SHOP OWNER":
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
        return render(request, "add_update.html", context)
    return redirect("404")


@login_required(login_url="signup")
def update_doctors_checkup_details(request, pk):
    if request.user.role == "SHOP OWNER":
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
        return render(request, "add_update.html", context)
    return redirect("404")


@login_required(login_url="signup")
def delete_doctors_checkup_details(request, pk):
    if request.user.role == "SHOP OWNER":

        to_delete = get_object_or_404(Doctors, id=pk)
        to_delete.delete()
        messages.success(
            request, "Doctors Deleted SuccessFully", extra_tags="alert-success"
        )
        return redirect("shop_dashboard")
    return redirect("404")


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
    return render(request, "add_update.html", context)


@login_required(login_url="signup")
def update_token_checkup_details(request, pk):
    if request.user.role == "SHOP OWNER":
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
        return render(request, "add_update.html", context)
    return redirect("404")


@login_required(login_url="signup")
def delete_token_checkup_details(request, pk):
    if request.user.role == "SHOP OWNER":

        to_delete = get_object_or_404(Token, id=pk)
        to_delete.delete()
        messages.success(
            request, "Token Deleted SuccessFully", extra_tags="alert-success"
        )
        return redirect("shop_dashboard")
    return redirect("404")


# appointment


def view_appointment(request):
    today=timezone.now()
    tommorow= today + timedelta(days=1)
    context = {
        "page_title": "All Appointment",
        "checkups":Appointment.objects.filter(status="finished").count(),
        "appointments": Appointment.objects.all(),
        "form": AppointmentStatusForm,
        "count":Appointment.objects.filter(appointment_date=today).count(),
        "counts":Appointment.objects.filter(appointment_date=tommorow).count()
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

    context = {
        "page_title": "Appointment Booking",
        "form": form,
        "available_tokens": available_tokens,
    }
    return render(request, "add_update.html", context)


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


# def view_token_service_offered(request):
#     context={"all_tokens":TokenService.objects.all()}
#     return render (request,"view_checkup_doctors_tokens.html",context)


class BookingAppointment(LoginRequiredMixin, ListView):
    model = Appointment
    template_name = "user_checkup_booking.html"
    extra_context = {"page_title": "Booked Appointment"}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["appointments"] = Appointment.objects.filter(username=self.request.user)
        return context


@login_required(login_url="signup")
def update_appointment(request, pk):
    to_update = get_object_or_404(Appointment, id=pk)
    if request.method == "POST":
        form = BookingAppointmentForm(request.POST, instance=to_update)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Appointment Updated SuccessFully", extra_tags="alert-success"
            )
            return redirect("dashboard")
        else:
            for error_list in form.errors.values():
                for errors in error_list:
                    messages.error(request, errors, extra_tags="alert-success")
    context = {
        "page_title": "Edit Appointment",
        "form": BookingAppointmentForm(instance=to_update),
    }
    return render(request, "add_update.html", context)


@login_required(login_url="signup")
def delete_appointment(request, pk):
    to_delete = get_object_or_404(Appointment, id=pk)
    to_delete.delete()
    messages.success(
        request, "Appointment Cancel SuccessFully", extra_tags="alert-success"
    )
    return redirect("dashboard")


@login_required(login_url="signup")
def status_appointment(request, pk):
    to_update = get_object_or_404(Appointment, id=pk)
    if request.method == "POST":
        form = AppointmentStatusForm(request.POST,instance=to_update)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Appointment Status Updated SuccessFully",
                extra_tags="alert-success",
            )
            return redirect("dashboard")
        else:
            for error_list in form.errors.values():
                for errors in error_list:
                    messages.error(request, errors, extra_tags="alert-danger")
    context = {
        "page_title": " Appointment Status",
        "form": AppointmentStatusForm(instance=to_update),
    }
    return render(request, "add_update.html", context)
