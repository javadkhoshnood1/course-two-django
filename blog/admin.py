from django.contrib import admin
from .models import Post,Category
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title","published_date","status")
    search_fields = ["title","content"]
    list_filter = ("status",)
    date_hierarchy = "published_date"
    
    
    
admin.site.register(Category)
    
    