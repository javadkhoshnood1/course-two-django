from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
# Create your views here.
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password =request.POST["password"]
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"login successfully")
            return redirect("/")
            
            
    return render(request,"accounts/login.html")



def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"logout is successfully")
        return redirect("/")
    return redirect("/")


def signup_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        first_name = request.POST["first_name"]
        new_user = User.objects.create(username=username,password=password,email=email,first_name=first_name)
        if new_user is not None:
            
            login(request,new_user)
            new_user.set_password(password)
            new_user.save()
            messages.success(request,"account created and you must be login ")
            return redirect("/")
        else:
            messages.error(request,"account not created")
            return redirect("/")
    return render(request,"accounts/signup.html")