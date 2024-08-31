from django import template
from blog.models import Post
register = template.Library()
from django.utils import timezone




@register.inclusion_tag("home/last_post_home.html")
def last_post_home_page():
    time_now = timezone.now()
    last_posts = Post.objects.exclude(published_date__gt=time_now).filter(status=True).order_by("-published_date")[:5]
    return {"last_posts" :last_posts}