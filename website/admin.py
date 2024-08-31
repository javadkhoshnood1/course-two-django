from django.contrib import admin
from .models import Contact
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ["name","subject","created_date"]
    search_fields = ["name","subject"]
    list_filter = ["created_date"]
admin.site.register(Contact,ContactAdmin)