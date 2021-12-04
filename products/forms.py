from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

class RawProductForm(forms.Form):
    title = forms.CharField(label='', widget = forms.TextInput(
        attrs={"placeholder":'title'}))
    description = forms.CharField(widget=forms.Textarea(
        attrs={
        "class": "new-class-name two",
        "id": "my-id-text-area",
        "rows": 20,
        "columns": 20
    }))
    price = forms.DecimalField()