from django import template
from ..models import Post,Comment
from django.utils import timezone
from django.shortcuts import render,get_object_or_404

register = template.Library()



@register.simple_tag(name="count_comment_post")
def count_comment_post(pid):
    post_single = Post.objects.get(id=pid)
    comments = Comment.objects.filter(post=post_single.id,allow=True).count()
    return comments