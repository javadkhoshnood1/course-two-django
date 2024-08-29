from django import template
from ..models import Category,Post
register = template.Library()
from django.utils import timezone

@register.inclusion_tag("blog/category_sidebar.html")
def all_category_sidebar():
    category = Category.objects.all()
    return {
        "category": category
    }
    
    
    
@register.inclusion_tag("blog/last_post_sidebar.html")
def last_post_sidebar():
    time_now = timezone.now()
    last_posts = Post.objects.exclude(published_date__gt=time_now).filter(status=True).order_by("-published_date")
    return {"last_posts" :last_posts}