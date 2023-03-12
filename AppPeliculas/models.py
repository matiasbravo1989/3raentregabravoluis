from django.db import models

# Create your models here.

class Pelicula(models.Model):
    autor=models.CharField(max_length=40, default="")
    nombre=models.CharField(max_length=40)
    año=models.IntegerField()
    director=models.FloatField()
    reseña=models.TextField(max_length=240)

class Estreno(models.Model):
    
    nombre=models.CharField(max_length=40)
    fecha=models.DateField()
    imagen=models.ImageField(upload_to = "estrenos", null=True)
    
    
    
