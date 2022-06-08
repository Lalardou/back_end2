from django.db import models

# Create your models here.

class Marca(models.Model):
    nombre = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre

# FORMULARIO DE AGREGAR PELICULAS #
class AgregarProducto (models.Model):
    nombre = models.CharField(max_length=15)
    precio = models.IntegerField()
    descripcion = models.TextField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to="componentes", null=True)

    def __str__(self):
        return self.nombre