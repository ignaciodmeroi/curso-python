from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
   
    def __str__(self) -> str:
        return self.nombre+" "+str(self.camada)



class Estudiantes(models.Model):
    nombre = models.CharField(max_length=30) 
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    
    def __str__(self) -> str:
        return self.nombre+" "+self.apellido


class Profesor(models.Model):
    nombre = models.CharField(max_length=30) 
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)    

    def __str__(self) -> str:
        return self.nombre+" "+str(self.profesion)


class Entregable(models.Model):
    nombre = models.CharField(max_length=30) 
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField()

    def __str__(self) -> str:
        return self.nombre+" "+str(self.fechaDeEntrega)    