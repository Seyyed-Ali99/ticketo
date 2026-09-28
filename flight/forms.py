from django import forms
from .models import Ticket,Flight,Airline,Airport
from django.http import request

class AddAirportForm(forms.ModelForm):
    class Meta :
        model = Airport
        fields = ["name","city","coutry"]


class EditAirportForm(forms.ModelForm):
    class Meta :
        model = Airport
        fields = ["name","city","coutry"]


class AddAirlineForm(forms.ModelForm):
    class Meta :
        model = Airline
        fields = ["name"]


class EditAirlineForm(forms.ModelForm):
    class Meta :
        model = Airline
        fields = ["name"]


class AddFlightForm(forms.ModelForm):
    class Meta :
        model = Flight
        fields = ["airline","origin","destination","board_time","arrival_time","price","capacity"]


class EditFlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ["airline","origin","destination","board_time","arrival_time","price","capacity"]


class AddTicketForm(forms.ModelForm):
    c_user = request.user 

    class Meta :
        model = Ticket
        fields = ["flight","seat_num","booking_date"]


class BuyTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ["status"]


class CancelTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ["status"]


class EditTicketForm(forms.ModelForm):pass

    







