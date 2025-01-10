from django import forms
from .models import comment
class commentForm(forms.ModelForm):
    class Meta:
        model= comment
        exclude=["post"]
        labels={
            "user_name":"your Name",
             "user_email":"Your Emaill",
            "text":"Your comment",
           
            
        }
        