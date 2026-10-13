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
    pass

class AddAirlineView(LoginRequiredMixin,CreateView):
    pass

class AddFlightView(LoginRequiredMixin,CreateView):
    pass

class EditAirportView(LoginRequiredMixin,UpdateView):
    pass

class EditAirlineView(LoginRequiredMixin,UpdateView):
    pass

class EditFlightView(LoginRequiredMixin,UpdateView):
    pass

class DeleteAirportView(LoginRequiredMixin,DeleteView):
    pass

class DeleteAirlineView(LoginRequiredMixin,DeleteView):
    pass

class DeleteFlightView(LoginRequiredMixin,DeleteView):
    pass

class Home(View):
    pass