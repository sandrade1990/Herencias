from django.db import models

# Create your models here.
class Familiares(models.Model):
    
    nombre = models.CharField(max_length=40)
    Edad = models.IntegerField()
    FechaNacimiento = models.DateField()