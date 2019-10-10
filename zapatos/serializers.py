from rest_framework import serializers
from . import models


class ZapatoSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('nombre', 'talla', 'tipo', 'precio', 'descripcion', 'color', 'tipo_tacon', 'altura_tacon', 'altura_suela', 'capellada', 'forro', 'plantilla', 'suela', 'ocasion', 'peso', 'marca', 'accesorios',)
        model = models.Zapato

        