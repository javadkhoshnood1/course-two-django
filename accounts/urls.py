from django.urls import path
from . import views

app_name = "accounts"

urlpatterns =[
    path("login/",views.login_view,name="login"),
    path("logout/",views.logout_view,name="logout"),
    path("signup/",views.signup_view,name="signup"),
    path("resetpassword/",views.reset_password_view,name="reset_password"),
    path("resetpassword/confirmcode/<str:username>/",views.confirm_code_view,name="confirm_code")

    
]