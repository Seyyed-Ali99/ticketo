from django.contrib import admin
from .models import Airline,Airport,Flight,Ticket
# Register your models here.

@admin.register(Airport)
class AirportAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "city",
        "country",
        "code",
    )
    ordering = ("-id",)
    list_per_page = 10
    search_fields = ("name","city","country","code")
    list_filter = ("city","country")


@admin.register(Airline)
class AirlineAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "code",
    )
    ordering = ("-id",)
    list_per_page = 10
    search_fields = ("name","code")
    

@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = (
        "flight_num",
        "airline",
        "origin",
        "destination",
        "board_time",
        "arrival_time",
        "price",
        "capacity",
        "airplane_model",
    )
    ordering = ("-id",)
    list_per_page = 10
    search_fields = ("flight_num","airline","origin","destination","board_time","arrival_time","price","capacity","airplane_model")
    list_filter = ("price","capacity","arrival_time","board_time","origin","destination")

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = (
        "passenger",
        "flight",
        "booking_date",
        "status",
        "amount",
    )
    ordering = ("-id",)
    list_per_page = 10
    search_fields = ("passenger","flight","status","amount")
    list_filter = ("booking_date","status","amount")
