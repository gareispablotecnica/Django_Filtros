from django.db import models

# Create your models here.

class Editorial(models.Model):
    CodEditorial=models.AutoField(primary_key=True)
    Nombre=models.TextField(max_length=15)

    def __str__(self):
        self.Nombre


        
class Libros(models.Model):
    Codigo_Libro=models.AutoField(primary_key=True)
    Titulo=models.TextField(max_length=15)
    Cantidad=models.IntegerField()
    Precio=models.FloatField()
    CodEditorial=models.IntegerField()

    def __str__(self):
        self.Titulo


class Personajes(models.Model):
    Codigo=models.AutoField(primary_key=True)
    Nombre=models.TextField(max_length=30)
    Casa=models.TextField(max_length=15)
    Hechizo=models.TextField(max_length=20)
    Imagen=models.ImageField(upload_to="Personajes",null=True)

    def __int__(self):
        self.Codigo