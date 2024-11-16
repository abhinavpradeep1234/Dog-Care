from django.urls import path
from . import views

urlpatterns = [
    path("", views.Signup, name="signup"),
    path("users/Login", views.log_in, name="login"),
    path("users/Logout", views.log_out, name="logout"),
    path("Account/Home", views.home, name="home"),
    path("Account/Dashboard", views.dashboard, name="dashboard"),
    path(
        "Account/Shop owner/Dashboard",
        views.Shop_owner_dashboard,
        name="shop_dashboard",
    ),
    path("Account/Users/Dashboard", views.users_dashboard, name="users_dashboard"),
    path("view/users", views.view_users, name="view_users"),
    path("add/users", views.add_users, name="add_users"),
    path("update/users/<int:pk>", views.update_users, name="update_users"),
    path("delete/users/<int:pk>", views.delete_users, name="delete_users"),
    
    #notification
    path("view/Notification", views.view_notification, name="notification"),
    path("view/Notification/read", views.read_offers, name="is_read"),
    #offers
    
    path("view/offers", views.view_offers, name="view_offers"),
    path("add/offers", views.add_offers, name="add_offers"),
    path("delete/offers/<int:pk>", views.delete_offers, name="delete_offers"),
    path("403/", views.unauthorized, name="403"),

    
    
]
