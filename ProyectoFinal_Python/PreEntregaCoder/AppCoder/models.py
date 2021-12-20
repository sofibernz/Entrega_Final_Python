from django.db import models

# Create your models here.

class Productos(models.Model):

    nombreProd = models.CharField(max_length=40)
    precio = models.IntegerField()
    
class Clientes(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    codCliente = models.IntegerField()
    email = models.EmailField()
    
class Vendedores(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    jerarquia = models.CharField(max_length=30)