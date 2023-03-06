from django.contrib import admin
from .models import Estudiante,ListaAsistencias,Notas,Actividades
# Register your models here.

class formato(admin.ModelAdmin):
    fields = ['idestAsist','fechaAsist','valorAsist']

admin.site.register(Estudiante)
admin.site.register(ListaAsistencias,formato)
admin.site.register(Notas)
admin.site.register(Actividades)
