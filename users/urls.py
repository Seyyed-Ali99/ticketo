from django.urls import path
from .views import UserRegisterView,UserEmailLoginView,UserUpdateView,UserLogoutView,UserDeleteView,UserDashboardView,OrderDetailView,OrdersPageView

urlpatterns = [
    path("user_register/",UserRegisterView.as_view(),name="user_register"),
    path("email_login/",UserEmailLoginView.as_view(),name="email_login"),
    path("logout/",UserLogoutView.as_view(),name="logout"),

    path("user_update/",UserUpdateView.as_view(),name="user_update"),
    path("user_delete/",UserDeleteView.as_view(),name="user_delete"),

    path("user_dashboard/",UserDashboardView.as_view(),name="user_dashboard"),

    path("user_orders/",OrdersPageView.as_view(),name="user_orders"),
    path("ticket/<int:id>/",OrderDetailView.as_view(),name="ticket"),
]