from django import forms
from .models import *

class stuform(forms.ModelForm):
    class Meta:
        model=student1
        fields=['name','email','marks','address']
