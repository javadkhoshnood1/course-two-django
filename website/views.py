from django.shortcuts import render,redirect
from .forms import ContactForm
from django.contrib import messages
from .models import Contact

def contact_page_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, "add message in database")
        else:
            messages.error(request, "not saved message and try again")

    form = ContactForm()    
    return render(request,"website/contact.html",{"form":form})