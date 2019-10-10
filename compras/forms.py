from django import forms
from .models import Compra

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
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