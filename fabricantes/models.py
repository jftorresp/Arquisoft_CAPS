from django.db import models

# Create your models here.

class Fabricante(models.Model):
    nombre = models.CharField(max_length = 100)
    direccion = models.CharField(max_length = 100)
    numero_cuenta = models.IntegerField()
  
    def __str__(self):
        return '{}'.format(self.nombre)
