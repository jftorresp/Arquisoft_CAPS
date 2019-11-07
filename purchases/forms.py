from django import forms
from .models import Purchase

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = [
            'fecha',
            'cliente',
            'zapato',
        ]

        labels = {
            'fecha' : 'Fecha',
            'cliente' : 'Cliente',
            'zapato' : 'Zapato',
        }