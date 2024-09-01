from django.contrib import admin
from .models import Post,Category,Comment
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title","published_date","status")
    search_fields = ["title","content"]
    list_filter = ("status",)
    date_hierarchy = "published_date"
    
    
class CommentAdmin(admin.ModelAdmin):
    list_display = ("name","post","allow")
    search_fields = ["name","subject"]
    list_filter = ("allow","post")
    date_hierarchy = "created_date"
    
admin.site.register(Category)
admin.site.register(Comment,CommentAdmin)
    
    