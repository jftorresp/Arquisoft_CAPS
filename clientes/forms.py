from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        contrasena = forms.CharField(widget=forms.PasswordInput)
        fields = [
            'nombre',
            'telefono',
            'correo',
            'contrasena',
            'direccion',
            'ciudad',
        ]

        labels = {
            'nombre' : 'Nombre',
            'telefono' : 'Telefono',
            'correo' : 'Correo',
            'contrasena' : 'Contraseña',
            'direccion' : 'Dirección',
            'ciudad' : 'Ciudad',
        }

