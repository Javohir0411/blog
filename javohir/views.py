from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View

from .forms import UserRegistrationModelForm, UserLoginForm
# from .models import Profile, Post


class HomePageView(View):
    def get(self, request):
        return render(request, 'javohir/home.html')


class UserRegisterView(View):
    def get(self, request):
        form = UserRegistrationModelForm()
        return render(request, "javohir/register.html", {"form": form})

    def post(self, request):
        form = UserRegistrationModelForm(data=request.POST)
        if form.is_valid():
            messages.success(request, "User registered successfully")
            form.save()
            return redirect('javohir:login')
        else:
            return render(request, "javohir/register.html", {"form": form})


class UserLoginView(View):
    def get(self, request):
        form = UserLoginForm()
        return render(request, "javohir/login.html", {"form": form})

    def post(self, request):
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print(request.COOKIES)
                messages.success(request, "User logged in successfully")
                return redirect("javohir:home-page")
            else:
                messages.error(request, "Username or password is wrong")
                return redirect("javohir:login")
        else:
            return render(request, "javohir/login.html", {"form": form})


class UserLogoutView(View):
    def get(self, request):
        return render(request, "javohir/logout.html")

    def post(self, request):
        logout(request)
        messages.info(request, "User logged out successfully")
        return redirect('javohir:home-page')


class UserAboutView(View):
    def get(self, request):
        return render(request, "javohir/about.html")


class UserHomeView(View):
    def get(self, request):
        return render(request, "javohir/home.html")


class UserPostDetailView(View):
    def get(self, request):
        return render(request, "javohir/post_detail.html")


class UserPostConfirmDeleteView(View):
    def get(self, request):
        return render(request, "javohir/post_confirm_delete.html")


class UserPostsView(View):
    def get(self, request):
        return render(request, "javohir/user_posts.html")


class UserPostsFormView(View):
    def get(self, request):
        return render(request, "javohir/post_form.html")
