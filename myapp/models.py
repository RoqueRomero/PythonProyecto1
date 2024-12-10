from django.db import models


# Create your models here.
class Estudiante(models.Model):
    apellido = models.CharField(max_length=30)
    nombres = models.CharField(max_length=30)
    materia = models.CharField(max_length=30)
    comision = models.IntegerField()
    
    
def __str__(self):
    return f"{self.apellido} - {self.nombres} - {self.materia} - {self.comision}"
