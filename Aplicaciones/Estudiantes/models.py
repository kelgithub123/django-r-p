from django.db import models
from django.utils import timezone
from ..Cursos.models import * 

# Create your models here.
class Estudiante(models.Model):
    idest=models.AutoField(primary_key=True)
    idcur=models.ForeignKey(Curso,on_delete=models.CASCADE)
    nombre=models.CharField(max_length=20)
    paterno=models.CharField(max_length=20)
    materno=models.CharField(max_length=20)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.paterno)

class ListaAsistencias(models.Model):
    idasist=models.AutoField(primary_key=True)
    idest4lista=models.ForeignKey(Estudiante,on_delete=models.CASCADE)
    fecha=models.DateTimeField(default=timezone.now, editable=False)
    permisos=models.CharField(max_length=1)

    def __str__(self):
        texto = "{0} ({1}) {2}"
        return texto.format(self.idasist, self.idest4lista.idest,self.fecha)