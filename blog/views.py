from django.shortcuts import render,get_object_or_404
from .models import Post
from django.utils import timezone
# Create your views here.


def all_blogs_view(request):
    time_now = timezone.now()
    posts = Post.objects.exclude(published_date__gt=time_now).filter(status=True)
    return render(request,"blog/all_blog.html",{"posts" :posts})



def single_blog(request,id):
    time_now = timezone.now()
    posts = Post.objects.exclude(published_date__gt=time_now).filter(status=True)
    post_single = get_object_or_404(posts,id=id)
    post_single.counted_view += 1
    post_single.save()
    post_next = ""
    post_prev = ""
    for item in posts:
        if item.id > post_single.id and Post.objects.filter(id=item.id,status=True):
            post_next = get_object_or_404(Post,id=item.id)
            print(post_next.id)
            break
        elif item.id < post_single.id and Post.objects.filter(id=item.id,status=True):
            post_prev = get_object_or_404(Post,id=item.id)
            print(post_prev.id)
    return render(request,"blog/single_blog.html",{"post" :post_single ,"post_prev":post_prev,"post_next":post_next})