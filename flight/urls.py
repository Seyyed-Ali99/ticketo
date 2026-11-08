from django.urls import path
from .views import AddAirportView,AddAirlineView,AddFlightView,EditAirportView,EditAirlineView,EditFlightView,DeleteAirlineView,DeleteAirportView,DeleteFlightView,Home,AirlineInformationView,AirlinesFlightView,ShowFlightView

urlpatterns = [
    path("",Home.as_view(),name="home"),

    path("add_airport/",AddAirportView.as_view(),name="add_airport"),
    path("add_airline/",AddAirlineView.as_view(),name="add_airline"),
    path("add_flight/",AddFlightView.as_view(),name="add_flight"),

    path("edit_airport/",EditAirportView.as_view(),name="edit_airport"),
    path("edit_airline/",EditAirlineView.as_view(),name="edit_airline"),
    path("edit_flight/",EditFlightView.as_view(),name="edit_flight"),

    path("delete_airport/",DeleteAirportView.as_view(),name="delete_airport"),
    path("delete_airline/",DeleteAirlineView.as_view(),name="delete_airline"),
    path("delete_flight/",DeleteFlightView.as_view(),name="delete_flight"),

    path("airline_information/<int:id>/",AirlineInformationView.as_view(),name="airline_info"),
    path("airline_flights/<int:id>/",AirlinesFlightView.as_view(),name="airline_flights"),
    path("show_flight/<int:id>/",ShowFlightView.as_view(),name="show_flight"),



]