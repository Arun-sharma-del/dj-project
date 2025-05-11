from django import forms
from .models import Order



class CheckoutForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name =  forms.CharField(max_length=100)
    email = forms.EmailField()
    address = forms.CharField(widget=forms.Textarea)
    city = forms.CharField(max_length=100)


