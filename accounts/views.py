from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
# Create your views here.
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == "POST":
       username = request.POST.get("username")
       password = request.POST.get("password")
       
       if "@" in username:
           user = User.objects.get(email=username)
           user_auth = authenticate(request,username=user.username,password=password)
           if user is not None and user_auth:
               login(request,user)
               messages.success(request,"login with email")
               return redirect("/")
           else:
               messages.error(request,"email not found")
       else:
            user = authenticate(request,username=username,password=password)
            if user is not None:
               login(request,user)
               messages.success(request,"login with username")
               return redirect("/")
            else:
                messages.error(request,"user not found")
        

                
    return render(request,"accounts/login.html")


@login_required
def logout_view(request):
    logout(request)
    messages.success(request,"logout is successfully")
    return redirect("/")


def signup_view(request):
    if not request.user.is_authenticated:
        
        if request.method == "POST":
            email= request.POST.get("email")
            username = request.POST.get("username")
            password = request.POST.get("password")
            
            if email and password and username:
                new_user = User.objects.create_user(username=username,email=email,password=password)
                login(request,new_user)
                messages.success(request,"accounts created")
                return redirect("/")
            else:
                messages.error(request," please enter all fields")
                
        return render(request,"accounts/signup.html")    
    else:       
        return render(request,"accounts/signup.html")