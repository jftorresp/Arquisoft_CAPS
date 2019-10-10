from django.db import models
from clientes.models import Cliente
from zapatos.models import Zapato

# Create your models here.

class Compra(models.Model):
    fecha = models.DateField()
    zapato = models.ManyToManyField(Zapato)
    cliente = models.ManyToManyField(Cliente)

    def __str__(self):
        return '{}'.format(self.fecha)
