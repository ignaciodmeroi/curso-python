from django.db import models

# Create your models here.

class Paciente(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dni = models.IntegerField()
    email = models.EmailField()

    def __str__(self) -> str:
        return self.apellido+" "+self.nombre+" "+str(self.dni)

class Profesional(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    especialidad = models.CharField(max_length=40)
    matricula = models.IntegerField()
    email = models.EmailField()

    def __str__(self) -> str:
        return self.apellido+" "+self.nombre+" "+self.especialidad

class Asistente(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    nempleado = models.IntegerField()
    email = models.EmailField()
    
    def __str__(self) -> str:
        return self.apellido+" "+self.nombre+" "+str(self.nempleaado)