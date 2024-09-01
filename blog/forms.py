from typing import Any
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    
    
    class Meta :
        model = Comment
        fields = ["name","subject","message","email","post"]