from django.db import models

# Create your models here.
class Curso(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    creditos = models.PositiveSmallIntegerField()

    def __str__(self):
        texto = "{0}{1}"
        return texto.format(self.codigo,self.nombre)