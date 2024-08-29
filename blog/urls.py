from django.urls import path 
from . import views

app_name = "blog"

urlpatterns =[
    path("",views.all_blogs_view,name="all"),
    path("<int:id>/",views.single_blog,name="single")
]