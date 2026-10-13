from django.shortcuts import render,redirect
from .models import SUser
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse , HttpResponseBadRequest,HttpResponseForbidden
from .forms import UserRegisterForm , EmailUserLoginForm , UserEditForm 
from django.contrib.auth.views import LogoutView , LoginView
from django.views import View
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, FormView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Avg , Sum

# Create your views here.

class UserRegisterView(CreateView):
    pass

class UserEmailLoginView(LoginView):
    pass

class UserUpdateView(UpdateView):
    pass

class UserLogoutView(LogoutView):
    pass

class UserDeleteView(DeleteView):
    pass

