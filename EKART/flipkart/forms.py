from django import forms
from .models import Customer

class User(forms.ModelForm):
    class Meta:
        model= Customer
        fields = '__all__'
        widgets = {
            'customer_name':forms.TextInput(attrs={'class':'form-control'}),
            'customer_id':forms.NumberInput(attrs={'class':'form-control'}),
            'customer_email':forms.EmailInput(attrs={'class':'form-control'}),
            'customer_phono': forms.NumberInput(attrs={'class': 'form-control'}),
            'customer_addrs': forms.TextInput(attrs={'class': 'form-control'}),

        }
