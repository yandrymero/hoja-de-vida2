from django.db import models
from django.core.validators import MinValueValidator


class Perfil(models.Model):
    foto = models.ImageField(upload_to='perfil/', blank=True, null=True)

    def __str__(self):
        return "Perfil principal"


class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    institucion = models.CharField(max_length=100)
    fecha = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='cursos/', blank=True, null=True)

    def __str__(self):
        return self.nombre


class Experiencia(models.Model):
    puesto = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    fecha = models.CharField(max_length=50)

    def __str__(self):
        return self.puesto



class ProductoAcademico(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.titulo



class ProductoLaboral(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='productos_laborales/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.titulo



class Reconocimiento(models.Model):
    titulo = models.CharField(max_length=100)
    fecha = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='reconocimientos/', blank=True, null=True)

    def __str__(self):
        return self.titulo


class VentaGaraje(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    imagen = models.ImageField(upload_to='ventas/', blank=True, null=True)

    def __str__(self):
        return self.nombre


