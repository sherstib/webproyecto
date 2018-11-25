from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Lenguajes(models.Model):
    id_lenguaje = models.AutoField(primary_key=True)
    nombre_lenguaje = models.CharField(max_length = 200)

    def __str__(self):
        return "{}" . format(self.nombre_lenguaje)


class Temas(models.Model):
    id_tema = models.AutoField(primary_key=True)
    nombre_tema = models.CharField(max_length = 200)
    contenido = models.CharField(max_length = 200)
    id_lenguaje = models.ForeignKey(Lenguajes, on_delete=models.CASCADE)

    def __str__(self):
        return "{}({}){}" .format(self.nombre_lenguaje, self.nombre_tema, self.contenido)


class Ejercicios(models.Model):
    id_ejercicio = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length = 200)
    contenido = models.CharField(max_length = 200)
    id_tema = models.ForeignKey(Temas, on_delete=models.CASCADE)

    def __str__(self):
        return "{}({}){}" .format(self.nombre_lenguaje, self.nombre_tema, self.contenido)