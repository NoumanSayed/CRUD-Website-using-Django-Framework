
from .models import footwear
from django import forms

class FootwearForm(forms.ModelForm):
    class Meta:
        model=footwear
        fields = ["name","brand","category","size","color","material","price","stock","description","image"]