from typing import Any
from django import forms
from .models import Contact

# class ContactForms(forms.Form):
#     name = forms.CharField(max_length=255)
#     email = forms.EmailField()
#     subject = forms.CharField(max_length=255)
#     message = forms.CharField(widget=forms.Textarea)


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name" ,"email","message","subject"]
        
    def clean(self):
        self.cleaned_data["name"] = "ناشناس"
        return super().clean()
    