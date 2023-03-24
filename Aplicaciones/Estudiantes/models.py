from django.db import models
from django.utils import timezone,dates
from ..Cursos.models import * 
import datetime
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
    fecha=datetime.date.today()
    format = fecha.strftime('%Y'+'-'+'%m'+'-'+'%d')
    idAsist=models.AutoField(primary_key=True)
    ideCurAsist=models.ForeignKey(Curso,default=None,on_delete=models.CASCADE,editable=True)
    idestAsist=models.ForeignKey(Estudiante,on_delete=models.CASCADE)
    fechaAsist=models.DateField(default=fecha, editable=True)
    valorAsist=models.FloatField(default=0)
    def __str__(self):
        texto = "{0} ({1}) {2} {3}"
        return texto.format(self.idAsist, self.idestAsist,self.valorAsist, self.ideCurAsist)

# class asistencia():
#     id=models.AutoField(models.Model)
#     fecha=models.models.DateTimeField(editable=True)
#     curso=models.ForeignKey(Curso,on_delete=models.CASCADE)

class Actividades(models.Model):
    idact=models.AutoField(primary_key=True)
    nombreAct=models.CharField(max_length=25)
    fechaAct=models.DateTimeField(editable=True)
    consignaAct=models.TextField(default='no instruida')
    def __str__(self):
        texto = "{0} ({1}) {2}"
        return texto.format(self.idact, self.nombreAct,self.fechaAct)

class Notas(models.Model):
    idnota=models.AutoField(primary_key=True)
    idestNota=models.ForeignKey(Estudiante,on_delete=models.CASCADE,default=None)
    idActNota=models.ForeignKey(Actividades,on_delete=models.CASCADE,default=None)
    valorNota=models.IntegerField()
    fechaNota=models.DateTimeField(default=timezone.now, editable=False)
    
    def __str__(self):
        texto = "{0} ({1}) {2} {3}"
        return texto.format(self.idnota, self.idActNota,self.fechaNota, self.valorNota)