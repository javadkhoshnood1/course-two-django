from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
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
        
        
class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "دسته بندی "
        verbose_name_plural = "دسته بندی ها" 