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
    model = SUser
    form_class = UserRegisterForm
    template_name = "user_template/user_register.html"
    success_url = reverse_lazy("")


class UserEmailLoginView(View):
    template_name = "user_email_login.html"

    def get(self,request):
        form = EmailUserLoginForm()
        return render(request , self.template_name , {"form":form})

    def post(self,request):
        form = EmailUserLoginForm(request.post)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate( username=username, password=password)


            if user:
                login(request, user)
                return redirect("")

            else:
                messages.error(request, 'Invalid email or password.')

            return render(request, self.template_name, {'form': form})
    

class UserUpdateView(LoginRequiredMixin,UpdateView):
    model = SUser
    form_class = UserEditForm
    template_name = "user_template/edit_user.html"
    success_url = reverse_lazy("")


class UserLogoutView(LoginRequiredMixin,View):
    login_url = 'login'
    def get(self,request):
        logout(request)
        return redirect('home')

class UserDeleteView(LoginRequiredMixin,DeleteView):
    model = SUser
    success_url = reverse_lazy("")
    template_name = "user_template/user_delete.html"

class UserDashboardView(LoginRequiredMixin,View):
    pass

class OrdersPageView(LoginRequiredMixin,View):
    pass
