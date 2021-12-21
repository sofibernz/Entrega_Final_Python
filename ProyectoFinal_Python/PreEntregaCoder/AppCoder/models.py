from django.db import models

# Create your models here.

class Productos(models.Model):

    nombreProd = models.CharField(max_length=40)
    precio = models.IntegerField()

    def __str__(self):

        return f"{self.nombreProd} - ${self.precio}"
    
class Clientes(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    codCliente = models.IntegerField()
    email = models.EmailField()

    def __str__(self):

        return f"Código: {self.codCliente} - Apellido y Nombre: {self.apellido}, {self.nombre} - Email: {self.email}"
    
class Vendedores(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    jerarquia = models.CharField(max_length=30)

    def __str__(self):

        return f"{self.apellido}, {self.nombre} - {self.jerarquia}"