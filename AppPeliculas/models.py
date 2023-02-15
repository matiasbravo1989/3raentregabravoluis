from django.db import models

# Create your models here.

class Pelicula(models.Model):

    nombre = models.CharField(max_length=50)
    año = models.IntegerField()
    director = models.CharField(max_length=50)
    genero= models.CharField(max_length=50)
    
