from django.shortcuts import render,redirect
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse,HttpResponseBadRequest,HttpResponseForbidden
from .models import Flight,Airline,Airport,Ticket
from .forms import AddAirportForm,AddAirlineForm,AddFlightForm,AddTicketForm,EditAirlineForm,EditAirportForm,EditFlightForm,EditTicketForm,BuyTicketForm,CancelTicketForm
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, FormView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.

class AddAirportView(LoginRequiredMixin,CreateView):
    model = Airport
    form_class = AddAirportForm
    template_name = "flight_template/add_airport.html"
    success_url = reverse_lazy("")


class AddAirlineView(LoginRequiredMixin,CreateView):
    model = Airline
    form_class = AddAirlineForm
    template_name = "flight_template/add_airline.html"
    success_url = reverse_lazy("")


class AddFlightView(LoginRequiredMixin,CreateView):
    model = Flight
    form_class = AddFlightForm
    template_name = "flight_template/add_flight.html"
    success_url = reverse_lazy("")


class EditAirportView(LoginRequiredMixin,UpdateView):
    model = Airport
    form_class = EditAirportForm
    template_name = "flight_template/edit_airport.html"
    success_url = reverse_lazy("")

class EditAirlineView(LoginRequiredMixin,UpdateView):
    model = Airline
    form_class = EditAirlineForm
    template_name = "flight_template/edit_airline.html"
    success_url = reverse_lazy("")

class EditFlightView(LoginRequiredMixin,UpdateView):
    model = Flight
    form_class = EditFlightForm
    template_name = "flight_template/edit_flight.html"
    success_url = reverse_lazy("")

class DeleteAirportView(LoginRequiredMixin,DeleteView):
    model = Airport
    template_name = "flight_template/delete_airport.html"
    success_url = reverse_lazy("")


class DeleteAirlineView(LoginRequiredMixin,DeleteView):
    model = Airline
    template_name = "flight_template/delete_airline.html"
    success_url = reverse_lazy("")

class DeleteFlightView(LoginRequiredMixin,DeleteView):
    model = Flight
    template_name = "flight_template/delete_flight.html"
    success_url = reverse_lazy("")
    
class Home(View):
    def get(self,*args,**kwargs):
        flights = Flight.objects.filter()


class AirlineInformationView(View):
    pass

class AirlinesFlightView(View):
    pass


class ShowFlightView(View):
    pass

class OrderTicketView(LoginRequiredMixin,View):
    pass

class CancelTicketView(LoginRequiredMixin,View):
    pass
