from django import forms
from .models import Movies

class MovieForms(forms.ModelForm):
    class Meta:
        model=Movies
        fields=['name','discription','year','img']