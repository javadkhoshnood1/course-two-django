from django.shortcuts import render,get_object_or_404
from .models import Post
# Create your views here.


def all_blogs_view(request):
    return render(request,"blog/all_blog.html")



def single_blog(request,id):
    post = get_object_or_404(Post,id=id,status=True)
    return render(request,"blog/single_blog.html",{"post" :post})