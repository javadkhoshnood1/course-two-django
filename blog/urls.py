from django.urls import path 
from . import views

app_name = "blog"

urlpatterns =[
    path("",views.all_blogs_view,name="all"),
    path("<int:id>/",views.single_blog,name="single"),
    path("category/<str:cat_name>/",views.all_blogs_view,name="category"),
    path("author/<str:username>/",views.all_blogs_view,name="author"),
    path("search/",views.search_blog_view,name="search"),


]