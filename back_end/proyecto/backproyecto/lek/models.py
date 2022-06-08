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

# CONSULTAS CONTACTO #
opciones_consultas = [
    [0, "Consultas"],
    [1, "Sugerencias"],
    [2, "Recuperacion"],
    [3, "Agradecimientos"]
]      

# FORMULARIO DE CONTACTO #
class Contactos(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    avisos = models.BooleanField()
    
    def __str__(self):
        return self.nombre
