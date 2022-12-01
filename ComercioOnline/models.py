from django.db import models 
from django.conf.locale.es import formats as es_formats

es_formats.DATETIME_FORMAT = '%m-%Y'

# Create your models here.

class Vendedor(models.Model):
    nombre = models.CharField(max_length=50)
    DNI = models.IntegerField()
    email = models.EmailField()
    contrasenia = models.CharField(max_length=8)

class Comprador(models.Model):
    nombre = models.CharField(max_length=50)
    DNI = models.IntegerField()
    email = models.EmailField()
    contrasenia = models.CharField(max_length=8)
    direccion_de_envio = models.CharField(max_length=50)
    
class Producto(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    precio = models.IntegerField()
