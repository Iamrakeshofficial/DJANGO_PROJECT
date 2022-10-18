from django.core import validators
from django import forms
from .models import Product

class ProductInformation(forms.ModelForm):
 class Meta:
    model = Product
    fields = ['id', 'pid', 'pname', 'price', 'rating']

    widgets = {
        'pid': forms.TextInput(attrs={'class':'form-control'}),
        'pname': forms.TextInput(attrs={'class':'form-control'}),
        'price': forms.TextInput(attrs={'class':'form-control'}),
        'rating': forms.TextInput(attrs={'class':'form-control'}),
  }