from django.shortcuts import render, redirect
from .forms import (
    SignupForm,
    LoginForm,
    UserRegisterForm,
    OfferForm,
    ComplaintForm,
    ComplaintRespondForm,
    ProfileForm,
)

# from .models import CustomUser
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404
from users.utils import create_notification
from users.models import Notification, Offers, Complaints, CustomUser
from django.views.generic import ListView

# from users.utils import create_offers
from shop.models import (
    Accessories,
    BookingService,
    BookingFood,
    BookingAccessories,
    Appointment,
    ServiceOffered,
    DogFood,
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def Signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(
                request, "You Account Created Successfully ", extra_tags="alert-success"
            )
            return redirect("login")
        else:
            for error_list in form.errors.values():
                for errors in error_list:
                    messages.error(request, errors, extra_tags="alert-danger")
    context = {"page_title": "Sign Up", "form": SignupForm()}

    return render(request, "signup.html", context)


def log_in(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            try:
                user = CustomUser.objects.get(username=username)
            except CustomUser.DoesNotExist:
                messages.error(request, "Username Doesn't Exists")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You Logged in", extra_tags="alert-success")
                return redirect("home")
            else:
                messages.error(request, "Password Not Match", extra_tags="alert-danger")
        else:
            for error_list in form.errors.values():
                for errors in error_list:
                    messages.error(request, errors, extra_tags="alert-danger")
    context = {"page_title": "Login", "form": LoginForm()}
    return render(request, "login.html", context)


@login_required(login_url="signup")
def home(request):
    if request.user.is_authenticated:
        create_notification(request.user, "Welcomhhe Our App")
    context = {"page_title": "Home"}

    return render(request, "home.html", context)


def log_out(request):
    messages.success(request, "Logged Out", extra_tags="alert-success")

    return redirect("signup")


@login_required(login_url="signup")
def dashboard(request):
    if request.user.role == "SHOP OWNER":
        return redirect("shop_dashboard")
    elif request.user:
        return redirect("users_dashboard")


@login_required(login_url="signup")
def Shop_owner_dashboard(request):
    if request.user.role == "SHOP OWNER":
        user_count = CustomUser.objects.count()
        role_count = CustomUser.objects.filter(role="SHOP OWNER").count()
        accessories = Accessories.objects.all().count()  # Fetch all accessories

        context = {
            "page_title": "Shop Owner",
            "user_count": user_count,
            "role_count": role_count,
            "all_offers": Offers.objects.all().count(),
            "all_accessorie": accessories,
            "all_foods": DogFood.objects.all().count(),
            "all_service": ServiceOffered.objects.all().count(),
            "all_users": BookingService.objects.all().count(),
            "all_accessories": BookingAccessories.objects.all().count(),
            "all_food": BookingFood.objects.all().count(),
            "appointments": Appointment.objects.all().count(),
            "all_complaints": Complaints.objects.all().count(),
            "counts": Notification.objects.filter(
                is_read=False, username=request.user
            ).count(),
        }
        return render(request, "shop_owner_dashboard.html", context)
    return redirect("403")


class UserDashboardListview(LoginRequiredMixin, ListView):
    model = Appointment
    paginate_by = 3
    ordering = ["-id"]
    context_object_name = "appointments"
    template_name = "users_dashboard.html"

    def get_queryset(self):
        return Appointment.objects.filter(username=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "User DashBoard"
        context["counts"] = Notification.objects.filter(
            is_read=False, username=self.request.user
        ).count()

        return context


class UserListView(LoginRequiredMixin, ListView):
    model = CustomUser
    template_name = "view_users.html"
    context_object_name = "all_users"
    paginate_by = 8
    ordering = ["id"]

    def dispatch(self, request, *args, **kwargs):
        if request.user.role != "SHOP OWNER":
            return redirect("403")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["page_title"] = "All Registered User"
        context["counts"] = Notification.objects.filter(
            is_read=False, username=self.request.user
        ).count()

        return context


@login_required(login_url="signup")
def add_users(request):
    if request.user.role == "SHOP OWNER":

        if request.method == "POST":
            form = UserRegisterForm(request.GET)
            if form.is_valid():
                form.save()
                messages.success(
                    request, "Registered user successfully", extra_tags="alert-success"
                )
                if request.user.is_authenticated:
                    create_notification(request.user, "Welcomhhe Our App")
                return redirect("shop_dashboard")

            else:
                for error_list in form.errors.values():
                    for errors in error_list:
                        messages.error(request, errors, extra_tags="alert-danger")

        context = {
            "page_title": "Register User",
            "form": UserRegisterForm(),
            "counts": Notification.objects.filter(
                is_read=False, username=request.user
            ).count(),
        }

        return render(request, "add_update_users.html", context)
    return redirect("403")


@login_required(login_url="signup")
def update_users(request, pk):
    to_update = get_object_or_404(CustomUser, id=pk)
    if request.method == "POST":
        form = UserRegisterForm(request.POST, instance=to_update)
        if form.is_valid():
            form.save()
            messages.success(
                request, "User Updated successfully", extra_tags="alert-success"
            )
            return redirect("shop_dashboard")
        else:
            for error_list in form.errors.values():
                for errors in error_list:
                    messages.error(request, errors, extra_tags="alert-danger")
    context = {
        "page_title": "Register User",
        "form": UserRegisterForm(instance=to_update),
        "counts": Notification.objects.filter(
            is_read=False, username=request.user
        ).count(),
    }

    return render(request, "add_update_users.html", context)


@login_required(login_url="signup")
def delete_users(request, pk):
    if request.user.role == "SHOP OWNER":
        to_delete = get_object_or_404(CustomUser, id=pk)
        to_delete.delete()
        messages.success(
            request, "Users Deleted Successfully", extra_tags="alert-success"
        )

        return redirect("view_users")
    return redirect("403")


# notification
@login_required(login_url="signup")
def view_notification(request):
    context = {
        "page_title": "View Notification",
        "all_notifications": Notification.objects.filter(
            username=request.user
        ).order_by("-id"),
        "counts": Notification.objects.filter(
            is_read=False, username=request.user
        ).count(),
    }
    return render(request, "notification.html", context)


@login_required(login_url="signup")
def read_offers(request, pk):
    notification = get_object_or_404(Notification, id=pk)
    notification.is_read = True
    notification.save()
    return redirect("notification")


# offers
@login_required(login_url="signup")
def view_offers(request):
    context = {
        "page_title": "All Offers",
        "form": OfferForm(),
        "all_offers": Offers.objects.all().order_by("-id"),
        "counts": Notification.objects.filter(
            is_read=False, username=request.user
        ).count(),
    }

    return render(request, "add_view_offers.html", context)


@login_required(login_url="signup")
def add_offers(request):
    if request.user.role == "SHOP OWNER":
        if request.method == "POST":
            form = OfferForm(request.POST)
            if form.is_valid():
                offers = form.save(commit=False)
                offers.username = (
                    request.user
                )  # Ensure this field exists in the Offers model
                offers.save()

                messages.success(
                    request, "Offers Added Successfully", extra_tags="alert-success"
                )
                all_user = CustomUser.objects.all()
                for user in all_user:
                    create_notification(
                        user,
                        " A brand-new offer has just been added. Don't miss out on exclusive deals and discounts. Check it out now!",
                    )
                return redirect("shop_dashboard")

            else:

                for error_list in form.errors.values():
                    for error in error_list:
                        messages.error(request, error, extra_tags="alert-danger")

        context = {
            "page_title": "View Offers",
            "form": form,
            "counts": Notification.objects.filter(
                is_read=False, username=request.user
            ).count(),
        }
        return render(request, "add_view_offers.html", context)
    return redirect("403")


@login_required(login_url="signup")
def delete_offers(request, pk):
    if request.user.role == "SHOP OWNER":
        to_delete = get_object_or_404(Offers, id=pk)
        to_delete.delete()
        messages.success(
            request, "Offers Deleted Successfully", extra_tags="alert-success"
        )
        return redirect("shop_dashboard")
    return redirect("403")


@login_required(login_url="signup")
def unauthorized(request):
    context = {"page_title": "403"}
    return render(request, "404.html", context)


class ComplaintListView(LoginRequiredMixin, ListView):
    model = Complaints
    template_name = "view_complaints.html"
    context_object_name = "all_bookings"
    paginate_by = 6
    ordering = ["-id"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "View Complaints"
        context["all_bookings"] = Complaints.objects.filter(username=self.request.user)
        context["counts"] = Notification.objects.filter(
            is_read=False, username=self.request.user
        ).count()

        return context


@login_required(login_url="signup")
def add_complaints(request):
    if request.method == "POST":
        form = ComplaintForm(request.POST)
        if form.is_valid():
            complaints = form.save(commit=False)
            complaints.username = request.user
            complaints.save()
            messages.success(
                request, "Complaint Registered Successfully", extra_tags="alert-success"
            )
            create_notification(request.user, "Complaint Registerd  Successfully")
            admin_users = CustomUser.objects.filter(role="SHOP OWNER")
            for admin_user in admin_users:
                create_notification(
                    admin_user,
                    f" {request.user} have registered a complaint check it now",
                )

            return redirect("view_complaints")
        else:
            for error_list in form.errors.values():
                for errors in error_list:
                    messages.error(request, errors, extra_tags="alert-danger")
    context = {
        "page_title": "Register complaint",
        "form": ComplaintForm,
        "counts": Notification.objects.filter(
            is_read=False, username=request.user
        ).count(),
    }
    return render(request, "add_update_users.html", context)


@login_required(login_url="signup")
def update_complaints(request, pk):
    to_update = get_object_or_404(Complaints, id=pk)
    if request.method == "POST":
        form = ComplaintForm(request.POST, instance=to_update)
        if form.is_valid():
            form.save()

            messages.success(
                request, "Complaint Updated Successfully", extra_tags="alert-success"
            )
            return redirect("view_complaints")
        else:
            for error_list in form.errors.values():
                for errors in error_list:
                    messages.error(request, errors, extra_tags="alert-danger")
    context = {
        "page_title": "Updated complaint",
        "form": ComplaintForm(instance=to_update),
        "counts": Notification.objects.filter(
            is_read=False, username=request.user
        ).count(),
    }
    return render(request, "add_update_users.html", context)


@login_required(login_url="signup")
def delete_complaints(request, pk):
    to_delete = get_object_or_404(Complaints, id=pk)
    to_delete.delete()
    messages.success(
        request, "Complaint Deleted Successfully", extra_tags="alert-success"
    )
    return redirect("view_complaints")


@login_required(login_url="signup")
def respond(request, pk):
    if request.user.role == "SHOP OWNER":
        to_update = get_object_or_404(Complaints, id=pk)
        notify = to_update.username
        if request.method == "POST":
            form = ComplaintRespondForm(request.POST, instance=to_update)
            if form.is_valid():
                form.save()

                messages.success(
                    request,
                    "Complaint Updated Successfully",
                    extra_tags="alert-success",
                )
                #
                create_notification(notify, "Authority respond your complaint")
                return redirect("shop_dashboard")
            else:
                for error_list in form.errors.values():
                    for errors in error_list:
                        messages.error(request, errors, extra_tags="alert-danger")
        context = {
            "page_title": "Complaint Responds",
            "form": ComplaintRespondForm(instance=to_update),
            "counts": Notification.objects.filter(
                is_read=False, username=request.user
            ).count(),
        }
        return render(request, "add_update_users.html", context)
    return redirect("403")


class AllComplaintListView(LoginRequiredMixin, ListView):
    model = Complaints
    template_name = "all_complaints.html"
    context_object_name = "all_bookings"
    paginate_by = 6
    ordering = ["-id"]

    def dispatch(self, request, *args, **kwargs):
        if request.user.role != "SHOP OWNER":
            return redirect("403")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "All Complaints"
        context["counts"] = Notification.objects.filter(
            is_read=False, username=self.request.user
        ).count()

        return context


@login_required(login_url="signup")
def profile(request):
    context = {
        "page_title": "Profile",
        "counts": Notification.objects.filter(
            is_read=False, username=request.user
        ).count(),
    }
    return render(request, "profile.html", context)


@login_required(login_url="signup")
def profile_update(request, pk):
    to_update = get_object_or_404(CustomUser, id=pk)
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=to_update)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Profile  Updated SuccessFully", extra_tags="alert-success"
            )
            return redirect("profile")
        else:
            for error_list in form.errors.values():
                for errors in error_list:
                    messages.error(request, errors, extra_tags="alert-danger")
    context = {
        "page_title": "Profile Update",
        "form": ProfileForm(instance=to_update),
        "counts": Notification.objects.filter(
            is_read=False, username=request.user
        ).count(),
    }
    return render(request, "add_update_users.html", context)
