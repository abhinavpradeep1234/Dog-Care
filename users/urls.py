from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.Signup, name="signup"),
    path("users/Login", views.log_in, name="login"),
    path("users/Logout", views.log_out, name="logout"),
    path("account/Home", views.home, name="home"),
    path("account/Dashboard", views.dashboard, name="dashboard"),
    path(
        "account/Shop_owner/dashboard",
        views.Shop_owner_dashboard,
        name="shop_dashboard",
    ),
    path("account/Users/dashboard", views.UserDashboardListview.as_view(), name="users_dashboard"),
    path("view/users", views.UserListView.as_view(), name="view_users"),
    path("add/users", views.add_users, name="add_users"),
    path("update/users/<int:pk>", views.update_users, name="update_users"),
    path("delete/users/<int:pk>", views.delete_users, name="delete_users"),
    
    #notification
    path("view/Notification", views.view_notification, name="notification"),
    path("view/Notification/read/<int:pk>", views.read_offers, name="is_read"),
    #offers
    
    path("view/offers", views.view_offers, name="view_offers"),
    path("add/offers", views.add_offers, name="add_offers"),
    path("delete/offers/<int:pk>", views.delete_offers, name="delete_offers"),
    path("403/", views.unauthorized, name="403"),
    
    #for user
    path("view/complaints", views.ComplaintListView.as_view(), name="view_complaints"),
    path("add/complaints", views.add_complaints, name="add_complaints"),
    path("update/complaints/<int:pk>", views.update_complaints, name="update_complaints"),
    path("delete/complaints/<int:pk>", views.delete_complaints, name="delete_complaints"),

    #for admin all complaint& responds
    path("complaints/respond/<int:pk>", views.respond, name="create_respond"),
    path("all/complaints", views.AllComplaintListView.as_view(), name="all_complaints"),

    #profile
    path("profile/",views.profile,name="profile"),
    path("profile/update/<int:pk>",views.profile_update,name="profile_update"),
    #forget password
    path("password/reset",auth_views.PasswordResetView.as_view(template_name="registration/password_reset.html"),name="password_reset"),
    path("password/done",auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),
    path("reset/<uidb64>/<token>",auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path("password/reset/complete",auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete")

 
    
    
]
