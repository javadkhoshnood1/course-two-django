from django.urls import path
from . import views

app_name = "website"

urlpatterns = [
    path("contact/",views.contact_page_view,name="contact")
]