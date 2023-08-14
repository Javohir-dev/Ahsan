from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import redirect, render
from django.views import View

from .forms import UserCreateForm


class RegisterView(View):
    def get(self, request):
        create_form = UserCreateForm()
        context = {
            'form': create_form
        }
        return render(request, "users/register.html", context)
    
    def post(self, request):
        create_form = UserCreateForm(data=request.POST)
        if create_form.is_valid():
            create_form.save()
            username = create_form.cleaned_data['username']
            password = create_form.cleaned_data['password']

            messages.success(request, "You have been successfully Registered!")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("home")
        else:
            context = {
                'form': create_form
            }
            return render(request, "users/register.html", context)


class LoginView(View):
    def get(self, request):
        login_form = AuthenticationForm()
        return render(request, "users/login.html", {'login_form': login_form})
    
    def post(self, request):
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)

            messages.success(request, "You have been successfully Logged In!")
            return redirect('home')
        else:
            return render(request, "users/login.html", {'login_form': login_form})