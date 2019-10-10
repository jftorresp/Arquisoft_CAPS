from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length = 100)
    telefono = models.BigIntegerField()
    correo = models.CharField(max_length = 100)
    contrasena = models.CharField(max_length = 50, null = True)
    direccion = models.CharField(max_length = 100, null = True)
    ciudad = models.CharField(max_length = 100, null = True)

    def __str__(self):
        return '{}'.format(self.nombre)