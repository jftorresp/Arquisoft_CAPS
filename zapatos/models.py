from django.db import models
from tallas.models import Talla
from fabricantes.models import Fabricante

# Create your models here.

class Zapato(models.Model):
    nombre = models.CharField(max_length = 100)
    talla = models.ManyToManyField(Talla)
    imagen = models.CharField(max_length = 100, null=True)
    tipo = models.CharField(max_length = 50)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length = 250)
    color = models.CharField(max_length = 50)
    tipo_tacon = models.CharField(max_length = 50)
    altura_tacon = models.DecimalField(max_digits = 3, decimal_places = 1)
    altura_suela = models.DecimalField(max_digits = 3, decimal_places = 1)
    capellada = models.CharField(max_length = 50)
    forro = models.CharField(max_length = 50)
    plantilla = models.CharField(max_length = 50)
    suela = models.CharField(max_length = 50)
    ocasion = models.CharField(max_length = 50)
    peso = models.IntegerField()
    marca = models.ForeignKey(Fabricante, on_delete = models.CASCADE)
    accesorios = models.CharField(max_length = 50)

    def __str__(self):
        return '{}'.format(self.nombre)

