from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import timedelta
from django.utils import timezone
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import CustomUser, Notification

from users.utils import create_notification
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
    UpdateBookServiceOfferedForm,
    BookAccessoriesForm,
    BookFoodForm,
    UpdateBookFoodForm,
    ServiceOfferedForm,
    AccessoriesForm,
    DogFoodForm,
    DoctorsForm,
    TokenForm,
    BookingAppointmentForm,
    UpdateBookAccessoriesForm,
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
        "counts": Notification.objects.filter(
            is_read=False, username=request.user
        ).count(),
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
                users = CustomUser.objects.all()
                for user in users:
                    create_notification(user, "New Service is Added check it now")
                return redirect("shop_dashboard")
            else:
                for error_list in form.errors.values():
                    for errors in error_list:
                        messages.error(request, errors, extra_tags="alert-danger")
        context = {
            "form": ServiceOfferedForm(),
            "page_title": "Add Service",
            "stock": True,
            "counts": Notification.objects.filter(
                is_read=False, username=request.user
            ).count(),
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
            "counts": Notification.objects.filter(
                is_read=False, username=request.user
            ).count(),
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
                users = CustomUser.objects.all()
                for user in users:
                    create_notification(user, "New Accessories is Added check it now")
                return redirect("shop_dashboard")
            else:
                for error_list in form.errors.values():
                    for errors in error_list:
                        messages.error(request, errors, extra_tags="alert-danger")
        context = {
            "page_title": "Add Accessories",
            "form": AccessoriesForm(),
            "total_stock": Accessories.objects.all(),
            "counts": Notification.objects.filter(
                is_read=False, username=request.user
            ).count(),
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
            "counts": Notification.objects.filter(
                is_read=False, username=request.user
            ).count(),
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
                users = CustomUser.objects.all()
                for user in users:
                    create_notification(user, "New Food Products is Added check it now")
                return redirect("shop_dashboard")
            else:
                for error_list in form.errors.values():
                    for errors in error_list:
                        messages.error(request, errors, extra_tags="alert-danger")
        context = {
            "page_title": "Add Food Products",
            "form": DogFoodForm(),
            "counts": Notification.objects.filter(
                is_read=False, username=request.user
            ).count(),
        }
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
            "counts": Notification.objects.filter(
                is_read=False, username=request.user
            ).count(),
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

        context = {
            "page_title": "Add Token",
            "form": ServiceTokenForm,
            "counts": Notification.objects.filter(
                is_read=False, username=request.user
            ).count(),
        }
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
            "counts": Notification.objects.filter(
                is_read=False, username=request.user
            ).count(),
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
            create_notification(
                request.user,
                f"Your {booking_service.service_name} Booking Successfully",
            )
            admins = CustomUser.objects.filter(role="SHOP OWNER")
            for admin in admins:
                create_notification(
                    admin,
                    f" The user {request.user} booked {booking_service.service_name} check it now",
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
        "counts": Notification.objects.filter(
            is_read=False, username=request.user
        ).count(),
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

                    create_notification(
                        request.user,
                        f"Your {books.accessories_name} Booking Successfully",
                    )
                    admins = CustomUser.objects.filter(role="SHOP OWNER")
                    for admin in admins:
                        create_notification(
                            admin,
                            f" The user {request.user} booked {books.accessories_name} check it now",
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
        "counts": Notification.objects.filter(
            is_read=False, username=request.user
        ).count(),
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
                    create_notification(
                        request.user,
                        f"Your {booking.Food_name} Booking Successfully",
                    )
                    admins = CustomUser.objects.filter(role="SHOP OWNER")
                    for admin in admins:
                        create_notification(
                            admin,
                            f" The user {request.user} booked {booking.Food_name} check it now",
                        )

                    return redirect("dashboard")

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
        "counts": Notification.objects.filter(
            is_read=False, username=request.user
        ).count(),
    }

    return render(request, "booking_dog_care.html", context)


# booked items admin list
class BookedServiceListView(LoginRequiredMixin, ListView):
    model = BookingService
    paginate_by = 6
    ordering = ["-id"]
    template_name = "service_booking.html"
    context_object_name = "all_users"

    def dispatch(self, request, *args, **kwargs):
        if request.user.role != "SHOP OWNER":
            return redirect("403")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "All  Service Booking"

        context["counts"] = Notification.objects.filter(
            is_read=False, username=self.request.user
        ).count()
        return context


class BookedAccessoriesListView(LoginRequiredMixin, ListView):
    model = BookingAccessories
    paginate_by = 6
    ordering = ["-id"]
    template_name = "accessories_booking.html"
    context_object_name = "all_accessories"

    def dispatch(self, request, *args, **kwargs):
        if request.user.role != "SHOP OWNER":
            return redirect("403")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "All  Accessories Booking"

        context["counts"] = Notification.objects.filter(
            is_read=False, username=self.request.user
        ).count()
        return context


class BookedFoodListView(LoginRequiredMixin, ListView):
    model = BookingFood
    paginate_by = 6
    ordering = ["-id"]
    template_name = "food_booking.html"
    context_object_name = "all_foods"

    def dispatch(self, request, *args, **kwargs):
        if request.user.role != "SHOP OWNER":
            return redirect("403")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "All  Food items  Booking"

        context["counts"] = Notification.objects.filter(
            is_read=False, username=self.request.user
        ).count()
        return context


#  Doctor/Token CRUD


class DoctorsListView(LoginRequiredMixin, ListView):
    template_name = "view_checkup_doctors_tokens.html"
    context_object_name = "all_doctors"
    paginate_by = 6
    ordering = ["id"]
    model = Doctors

    def dispatch(self, request, *args, **kwargs):
        if request.user.role != "SHOP OWNER":
            return redirect("403")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "All Doctors Details"

        context["counts"] = Notification.objects.filter(
            is_read=False, username=self.request.user
        ).count()

        return context


class TokenListView(LoginRequiredMixin, ListView):
    template_name = "all_tokens.html"
    context_object_name = "all_tokens"
    paginate_by = 6
    ordering = ["id"]
    model = Token

    def dispatch(self, request, *args, **kwargs):
        if request.user.role != "SHOP OWNER":
            return redirect("403")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "All CheckUp Token Details"
        context["counts"] = Notification.objects.filter(
            is_read=False, username=self.request.user
        ).count()

        return context


class TokenServiceListView(LoginRequiredMixin, ListView):
    template_name = "all_service_tokens.html"
    context_object_name = "all_tokens_services"
    paginate_by = 6
    ordering = ["id"]
    model = TokenService

    def dispatch(self, request, *args, **kwargs):
        if request.user.role != "SHOP OWNER":
            return redirect("403")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "All Service Token Details"

        context["counts"] = Notification.objects.filter(
            is_read=False, username=self.request.user
        ).count()

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

        context = {
            "page_title": "Add Doctors Details",
            "form": DoctorsForm(),
            "counts": Notification.objects.filter(
                is_read=False, username=request.user
            ).count(),
        }
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
            "counts": Notification.objects.filter(
                is_read=False, username=request.user
            ).count(),
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


@login_required(login_url="signup")
def add_token_checkup_details(request):
    if request.user.role == "SHOP OWNER":
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

        context = {
            "page_title": "Add Token Details",
            "form": TokenForm(),
            "counts": Notification.objects.filter(
                is_read=False, username=request.user
            ).count(),
        }
        return render(request, "add_update.html", context)
    return redirect("403")


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
            "counts": Notification.objects.filter(
                is_read=False, username=request.user
            ).count(),
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
class AppointmentListView(LoginRequiredMixin, ListView):
    model = Appointment
    form_class = AppointmentStatusForm
    template_name = "view_appointment.html"
    paginate_by = 6
    ordering = ["-id"]
    context_object_name = "appointments"

    def dispatch(self, request, *args, **kwargs):
        if request.user.role != "SHOP OWNER":
            return redirect("403")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        today = timezone.now().date()
        tommorow = today + timedelta(days=1)

        context = super().get_context_data(**kwargs)
        context["page_title"] = "All Appointment"
        context["checkups"] = Appointment.objects.filter(status="finished").count()
        context["count"] = Appointment.objects.filter(appointment_date=today).count()
        context["counts"] = Appointment.objects.filter(
            appointment_date=tommorow
        ).count()
        context["counts"] = Notification.objects.filter(
            is_read=False, username=self.request.user
        ).count()

        return context


from django.utils import timezone
from datetime import timedelta
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Token, TokenAvailability, Appointment
from shop.forms import BookingAppointmentForm


@login_required(login_url="signup")
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
                    create_notification(
                        request.user,
                        f"Your {appointment.Token} Booking Successfully",
                    )
                    admins = CustomUser.objects.filter(role="SHOP OWNER")
                    for admin in admins:
                        create_notification(
                            admin,
                            f" The user {request.user} booked token --{appointment.Token} in - {appointment.appointment_date} check it now",
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
        "counts": Notification.objects.filter(
            is_read=False, username=request.user
        ).count(),
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


# class BookingAppointment(LoginRequiredMixin, ListView):
#     model = Appointment
#     template_name = "user_checkup_booking.html"
#     extra_context = {"page_title": "Booked Appointment"}

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["appointments"] = Appointment.objects.filter(username=self.request.user)
#         return context


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
        "counts": Notification.objects.filter(
            is_read=False, username=request.user
        ).count(),
    }
    return render(request, "add_update.html", context)


@login_required(login_url="signup")
def delete_appointment(request, pk):
    # Get the appointment instance or return a 404
    to_delete = get_object_or_404(Appointment, id=pk)

    # Get the token and appointment date
    token = to_delete.Token
    appointment_date = to_delete.appointment_date

    # Delete the appointment
    to_delete.delete()

    # Update token availability for the specific date
    token_availability_entry = TokenAvailability.objects.filter(
        token=token, date=appointment_date
    ).first()

    if token_availability_entry:
        token_availability_entry.is_available = True  # Make the token available again
        token_availability_entry.save()

    # Display success message and redirect
    messages.success(
        request, "Appointment Cancelled Successfully", extra_tags="alert-success"
    )
    return redirect("dashboard")


@login_required(login_url="signup")
def status_appointment(request, pk):
    if request.user.role == "SHOP OWNER":
        to_update = get_object_or_404(Appointment, id=pk)
        notify = to_update.username
        if request.method == "POST":
            form = AppointmentStatusForm(request.POST, instance=to_update)
            if form.is_valid():
                form.save()
                messages.success(
                    request,
                    "Appointment Status Updated SuccessFully",
                    extra_tags="alert-success",
                )
                create_notification(
                    notify, f"Authority Change the  status  to {to_update.status}"
                )
                admins = CustomUser.objects.filter(role="SHOP OWNER")
                for admin in admins:
                    create_notification(admin, f"you change the status")
                return redirect("dashboard")
            else:
                for error_list in form.errors.values():
                    for errors in error_list:
                        messages.error(request, errors, extra_tags="alert-danger")
        context = {
            "page_title": " Appointment Status",
            "form": AppointmentStatusForm(instance=to_update),
            "counts": Notification.objects.filter(
                is_read=False, username=request.user
            ).count(),
        }
        return render(request, "add_update.html", context)
    return redirect("403")


# user booking display


class BookedService(LoginRequiredMixin, ListView):
    model = BookingService
    template_name = "booking_service.html"
    context_object_name = "all_user"
    paginate_by = 3
    ordering = ["-id"]

    def get_queryset(self):
        return BookingService.objects.filter(username=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Booked Service"
        # context["all_user"] = BookingService.objects.all().order_by("-id")
        context["counts"] = Notification.objects.filter(
            is_read=False, username=self.request.user
        ).count()

        return context


class BookedAccessories(LoginRequiredMixin, ListView):
    model = BookingAccessories
    template_name = "booking_accessories.html"
    context_object_name = "all_accessories"
    paginate_by = 3
    ordering = ["-id"]

    def get_queryset(self):
        return BookingAccessories.objects.filter(username=self.request.user).order_by(
            "-id"
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Booked Accessories"

        context["counts"] = Notification.objects.filter(
            is_read=False, username=self.request.user
        ).count()

        return context


class BookedFood(LoginRequiredMixin, ListView):
    model = BookingFood
    template_name = "booking_food.html"
    context_object_name = "all_food"
    paginate_by = 3
    ordering = ["-id"]

    def get_queryset(self):
        return BookingFood.objects.filter(username=self.request.user).order_by("-id")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Booked Food Products"
        context["counts"] = Notification.objects.filter(
            is_read=False, username=self.request.user
        ).count()

        return context


@login_required(login_url="signup")
def update_booking_service_offered(request, pk):
    to_update = get_object_or_404(BookingService, id=pk)
    if request.method == "POST":
        form = UpdateBookServiceOfferedForm(request.POST, instance=to_update)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Updated Successfully", extra_tags="alert-success"
            )
            return redirect("dashboard")
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(request, errors, extra_tags="alert-danger")

    context = {
        "page_title": "Update",
        "form": UpdateBookServiceOfferedForm(instance=to_update),
        "counts": Notification.objects.filter(
            is_read=False, username=request.user
        ).count(),
    }
    return render(request, "add_update.html", context)


@login_required(login_url="signup")
def delete_booking_service_offered(request, pk):
    to_delete = get_object_or_404(BookingService, id=pk)
    token_avilability = to_delete.token
    to_delete.delete()
    token_avilability.available = True

    token_avilability.save()
    messages.success(request, "Booking Cancel Successfully", extra_tags="alert-success")
    return redirect("dashboard")


@login_required(login_url="signup")
def update_booking_accessories(request, pk):
    to_update = get_object_or_404(BookingAccessories, id=pk)
    if request.method == "POST":
        form = UpdateBookAccessoriesForm(request.POST, instance=to_update)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Accessories Updated Successfully", extra_tags="alert-success"
            )
            return redirect("dashboard")
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(request, errors, extra_tags="alert-danger")

    context = {
        "page_title": "Edit Booking",
        "form": UpdateBookAccessoriesForm(instance=to_update),
        "counts": Notification.objects.filter(
            is_read=False, username=request.user
        ).count(),
    }
    return render(request, "add_update.html", context)


@login_required(login_url="signup")
def delete_booking_accessories(request, pk):
    to_delete = get_object_or_404(BookingAccessories, id=pk)
    to_delete.delete()
    messages.success(
        request, "Accessories Booking Cancel Successfully", extra_tags="alert-success"
    )
    return redirect("dashboard")


@login_required(login_url="signup")
def update_booking_food(request, pk):
    to_update = get_object_or_404(BookingFood, id=pk)
    if request.method == "POST":
        form = UpdateBookFoodForm(request.POST, instance=to_update)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Accessories Updated Successfully", extra_tags="alert-success"
            )
            return redirect("dashboard")
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(request, errors, extra_tags="alert-danger")

    context = {
        "page_title": "Update",
        "form": UpdateBookFoodForm(instance=to_update),
        "counts": Notification.objects.filter(
            is_read=False, username=request.user
        ).count(),
    }
    return render(request, "add_update.html", context)


@login_required(login_url="signup")
def delete_booking_food(request, pk):
    to_delete = get_object_or_404(BookingFood, id=pk)
    to_delete.delete()
    messages.success(
        request, "Booking Food item Cancel Successfully", extra_tags="alert-success"
    )
    return redirect("dashboard")
