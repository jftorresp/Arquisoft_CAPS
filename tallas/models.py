from django.db import models

# Create your models here.

class Talla(models.Model):
    numero =  models.DecimalField(max_digits = 3, decimal_places = 1)
    numero_uk = models.DecimalField(max_digits = 3, decimal_places = 1)
    numero_us = models.DecimalField(max_digits = 3, decimal_places = 1)

    def __str__(self):
        return '%s' % (self.numero)