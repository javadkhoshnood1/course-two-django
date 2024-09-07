from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
# Create your views here.
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse,reverse_lazy
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.decorators import login_required
from random import randint
from django.core.mail import EmailMessage, get_connection
from django.conf import settings
from .models import CodeConfirm
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
            password1 = request.POST.get("password1")
            password2 = request.POST.get("password2")

            if email and password1 and password2 and username:
                if password1 == password2:
                    new_user = User.objects.create_user(username=username,email=email,password=password1)
                    messages.success(request,"accounts created")
                    return redirect("/")
                else:
                    messages.error(request,"password1 and password 2 not same")
            else:
                messages.error(request," please enter all fields")
                
        return render(request,"accounts/signup.html")    
    else:       
        return render(request,"accounts/signup.html")
    
    
    
    
def reset_password_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST.get("username")
            print(username)
            if username:
                if "@" in username:
                        user = User.objects.get(email=username)
                        messages.success(request,"send code in email / please enter new password")
                        random_code = randint(1000,10000)
                        new_code = CodeConfirm.objects.create(user=user,code=random_code)
                        new_code.save()
                        send_email(new_code,user.email)
                        print(new_code.code)
                        return redirect(f"/accounts/resetpassword/confirmcode/{user.username}")
                 
                else:
                   
                    messages.error(request,"user with this username not found / please enter email")

                    
                        
            else:
               messages.error(request,"please enter all fields")
        return render(request,"accounts/reset_password.html")        
    return render(request,"accounts/reset_password.html")



def confirm_code_view(request,username):
    if request.method == "GET":
        user = User.objects.get(username=username)
    if request.method == "POST":
        user = User.objects.get(username=username)
        new_code = CodeConfirm.objects.get(user=user)
        code = request.POST.get("code")
        print(f"code {code}",f"new code  :{new_code.code}")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        if user and password1 and password2 and code:
            if int(code) == new_code.code :
                if password1 == password2 :
                    user.set_password(password1)
                    user.save()
                    new_code.delete()
                    messages.success(request,f"ok reset password {user.username}")
                    return redirect("/")
                else:
                    messages.error(request,"password1 and password2 not same")
    
            else:
                messages.error(request,"code confirm is not correct")        
    return render(request,"accounts/confirm_code.html" ,)




def send_email(random_code,email):  
    with get_connection(  
     host=settings.EMAIL_HOST, 
     port=settings.EMAIL_PORT,  
     username=settings.EMAIL_HOST_USER, 
     password=settings.EMAIL_HOST_PASSWORD, 
     use_tls=settings.EMAIL_USE_TLS  
       ) as connection:  
           subject = random_code
           email_from = settings.EMAIL_HOST_USER  
           recipient_list = [email, ]  
           message = f"code confirm :{random_code}"
           EmailMessage(subject, message, email_from, recipient_list, connection=connection).send()  
 
