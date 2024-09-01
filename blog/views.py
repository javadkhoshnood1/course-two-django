from django.shortcuts import render,get_object_or_404
from .models import Post
from django.utils import timezone
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.


def all_blogs_view(request,**kwargs):
    time_now = timezone.now()
    posts = Post.objects.exclude(published_date__gt=time_now).filter(status=True)
    cat_name = ""
    username = ""
    tag_name= ""
    if kwargs.get("cat_name") != None:
        cat_name = kwargs.get("cat_name")
        posts = posts.filter(category__name=kwargs.get("cat_name"))
    
    if kwargs.get("tag_name") != None:
        tag_name = kwargs.get("tag_name")
        print(tag_name)
        posts = posts.filter(tag__name__in=[kwargs.get("tag_name")])
        
    if kwargs.get("username") != None:
        username = kwargs.get("username")
        posts = posts.filter(author__username=kwargs.get("username"))
    
    posts = Paginator(posts,2)
    try :
        page_number = request.GET.get("page")
        posts = posts.get_page(page_number)
    
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage :
        posts = posts.get_page(1)
        
    
    return render(request,"blog/all_blog.html",{"posts" :posts,"cat_name":cat_name ,"username" :username,"tag_name":tag_name})



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



def search_blog_view(request):
    time_now = timezone.now()
    posts = Post.objects.exclude(published_date__gt=time_now).filter(status=True)
    if request.method == "GET":
        if s:= request.GET.get("search_word"):
            search_words = s
            posts = posts.filter(content__contains=s)
    
    return render(request,"blog/all_blog.html",{"posts" :posts,"search_word":search_words})
       
            
            