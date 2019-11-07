from django.db import models
from zapatos.models import Zapato
from clientes.models import Cliente

# Create your models here.

class Purchase(models.Model):
    fecha = models.DateField()
    zapato = models.ManyToManyField(Zapato)
    cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)

    def __str__(self):
        return '{}'.format(self.fecha)
