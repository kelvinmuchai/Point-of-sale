# forms.py
from django import forms
from .models import Products

from .models import Category



class ProductsUpdateForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['p_name','p_description','p_price','p_image']
        