from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
from taggit.managers import TaggableManager


class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    tag = TaggableManager()
    category = models.ManyToManyField('Category')
    image = models.ImageField(upload_to="blog_image",null=True)
    status = models.BooleanField(default=False)
    counted_view = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True,null=True)
    updated_date = models.DateTimeField(auto_now=True,null=True)
    published_date = models.DateTimeField(null=True)
    
    def __str__(self):
        return self.title
    class Meta:
        ordering = ["created_date"]
        verbose_name = "پست "
        verbose_name_plural = "پست ها "    
    
    def get_absolute_url(self):
        return reverse("blog:single",kwargs={"id":self.id})
        
class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "دسته بندی "
        verbose_name_plural = "دسته بندی ها" 