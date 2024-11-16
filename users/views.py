from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm, UserRegisterForm, OfferForm
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404
from users.utils import create_notification
from users.models import Notification, Offers
from users.utils import create_offers
from shop.models import Accessories, BookingService, BookingFood, BookingAccessories


def Signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(
                request, "You Account Created Succesfully ", extra_tags="alert-success"
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


def home(request):
    if request.user.is_authenticated:
        create_notification(request.user, "Welcome Our App")
    context = {"page_title": "Home"}

    return render(request, "home.html", context)


def log_out(request):
    messages.success(request, "Logged Out", extra_tags="alert-success")

    return redirect("signup")


def dashboard(request):
    if request.user.role == "SHOP OWNER":
        return redirect("shop_dashboard")
    elif request.user:
        return redirect("users_dashboard")


def Shop_owner_dashboard(request):
    user_count = CustomUser.objects.count()
    role_count = CustomUser.objects.filter(role="SHOP OWNER").count()
    accessories = Accessories.objects.all()  # Fetch all accessories

    context = {
        "page_title": "Shop Owner",
        "user_count": user_count,
        "role_count": role_count,
        "all_accessorie": accessories,
    }
    return render(request, "shop_owner_dashboard.html", context)


def users_dashboard(request):
    context = {
        "page_title": "User DashBoard",
        "all_users": BookingService.objects.all(),
        "all_accessories": BookingAccessories.objects.all(),
        "all_foods": BookingFood.objects.all(),
    }

    return render(request, "users_dashboard.html", context)


def view_users(request):
    context = {"page_title": "All Users", "all_users": CustomUser.objects.all()}
    return render(request, "view_users.html", context)


def add_users(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Registered user successfully", extra_tags="alert-success"
            )
            return redirect("shop_dashboard")
        else:
            for error_list in form.errors.values():
                for errors in error_list:
                    messages.error(request, errors, extra_tags="alert-danger")

    context = {"page_title": "Register User", "form": UserRegisterForm()}

    return render(request, "add_update_users.html", context)


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
    }

    return render(request, "add_update_users.html", context)


def delete_users(request, pk):
    to_delete = get_object_or_404(CustomUser, id=pk)
    to_delete.delete()
    messages.success(request, "Users Deleted Successfully", extra_tags="alert-success")

    return redirect("view_users")


# notification
def view_notification(request):
    context = {
        "page_title": "View Notification",
        "all_notifications": Notification.objects.filter(username=request.user),
    }
    return render(request, "notification.html", context)


def read_offers(request, pk):
    notification = get_object_or_404(Notification, id=pk)
    notification.is_read = True
    notification.save()
    return redirect("notification")


# offers
def view_offers(request):
    context = {
        "page_title": "All Offers",
        "form": OfferForm(),
        "all_offers": Offers.objects.all().order_by("-id"),
    }

    return render(request, "add_view_offers.html", context)


# def add_offers(request):
#     if request.method == "POST":
#         form = OfferForm(request.POST)
#         if form.is_valid():
#             offers = form.save(commit=False)
#             offers.username = request.user
#             form.save()

#             messages.success(
#                 request, "Offers Added  Successfully", extra_tags="alert-success"
#             )
#             notify=CustomUser.objects.filter(is_active=True)
#             offer=offers.save

#             if request.user.is_authenticated:
#                 create_offers(notify,offer)
#             return redirect("shop_dashboard")


#         else:
#             for error_list in form.errors.values():
#                 for errors in error_list:
#                     messages.success(request, errors, extra_tags="alert-danger")
#     context = {"page_title": "View Offers", "form": OfferForm()}
#     return render(request, "add_view_offers.html", context)
def add_offers(request):
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
            return redirect("shop_dashboard")
        else:
            # Print out form errors for debugging
            print(form.errors)  # Check the console for any validation issues
            for error_list in form.errors.values():
                for error in error_list:
                    messages.error(
                        request, error, extra_tags="alert-danger"
                    )  # Change to error

    else:
        form = OfferForm()  # Initialize a new form for GET requests

    context = {"page_title": "View Offers", "form": form}
    return render(request, "add_view_offers.html", context)


def delete_offers(request, pk):
    to_delete = get_object_or_404(Offers, id=pk)
    to_delete.delete()
    messages.success(request, "Offers Deleted Successfully", extra_tags="alert-success")
    return redirect("shop_dashboard")



def unauthorized(request):
    context={"page_title":"403"}
    return render(request,"404.html",context)