from django import forms
from .models import Zapato

class ZapatoForm(forms.ModelForm):
    class Meta:
        model = Zapato
        fields = [
            'nombre',
            'talla',
            'tipo',
            'precio',
            'descripcion',
            'color',
            'tipo_tacon',
            'altura_tacon',
            'altura_suela',
            'capellada',
            'forro',
            'plantilla',
            'suela',
            'ocasion',
            'peso',
            'marca',
            'accesorios',
        ]

        labels = {
            'nombre' : 'Nombre',
            'talla' : 'Talla',
            'tipo' : 'Tipo',
            'precio' : 'Precio',
            'descripcion' : 'Descripcion',
            'color' : 'Color',
            'tipo_tacon' : 'Tipo Tacon',
            'altura_tacon' : 'Altura Tacon',
            'altura_suela' : 'Altura Suela',
            'capellada' : 'Capellada',
            'forro' : 'Forro',
            'plantilla' : 'Plantilla',
            'suela' : 'Suela',
            'ocasion' : 'Ocasion',
            'peso': 'Peso (GR)',
            'marca' : 'Marca',
            'accesorios' : 'Accesorios',
        }
