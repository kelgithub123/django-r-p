from django.db import models
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
        return texto.format(self.nom, self.pat)