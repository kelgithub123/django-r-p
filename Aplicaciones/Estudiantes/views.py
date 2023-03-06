import datetime
from django.shortcuts import render,redirect
from .models import Estudiante,ListaAsistencias,Notas,Actividades
from ..Cursos.models import Curso
from django.contrib import messages
# Create your views here.

def homeEst(request):
    EstudListados = Estudiante.objects.all()
    cursos=Curso.objects.all()
    messages.success(request, '¡Estudiantes del curso!')
    return render(request, "gestionEst.html", {"Estudiantes": EstudListados, "cursos":cursos})

def ListaEstCurso(request,codigo):
    cursos=Curso.objects.all()
    EstudListados = Estudiante.objects.filter(idcur=codigo)
    messages.success(request, '¡Estudiantes del curso!')
    return render(request, "gestionEst.html", {"Estudiantes": EstudListados, "cursos":cursos, "curso":codigo})

def registro(request,curso):
    EstudListados = Estudiante.objects.filter(idcur=curso)
    fecha=datetime.date.today()
    Asistencias=ListaAsistencias.objects.filter(fechaAsist=fecha)
    return render(request, "RegistroEst.html",{"Estudiantes": EstudListados,"Asistentes":Asistencias})

def registrarEst(request):
    nom = request.POST['txtNombre']
    pat = request.POST['txtPaterno']
    mat = request.POST['txtMaterno']
    idcurso = Curso.objects.get(codigo=request.POST['txtCurso'])
    estudiante = Estudiante.objects.create(idcur=idcurso,nombre=nom,paterno=pat,materno=mat)
    messages.success(request, 'Estudiante registrado!')
    return redirect('/est/listaCurso/'+str(idcurso.codigo))

def edicionEst(request, codigo):
    cursos = Curso.objects.all()
    Est = Estudiante.objects.get(idest=codigo)
    return render(request, "edicionEst.html", {"Estudiante": Est, "curso":cursos})

def editarEst(request,idest):
    nom = request.POST['txtNombre']
    pat = request.POST['txtPaterno']
    mat = request.POST['txtMaterno']
    idcurso = Curso.objects.get(codigo=request.POST['txtCurso'])
    Est = Estudiante.objects.get(idest=idest)
    Est.nombre = nom
    Est.paterno = pat
    Est.materno = mat
    Est.idcur=idcurso
    Est.save()
    messages.success(request, '¡Datos actualizados!')
    return redirect('../listaCurso/'+str(idcurso.codigo))

def eliminarEst(request,codigo):
    Est = Estudiante.objects.get(idest=codigo)
    idcurso = Est.idcur
    Est.delete()
    messages.success(request, '¡Estudiante eliminado!')
    return redirect('/est/listaCurso/'+str(idcurso.codigo))

def registrarAsist(request,idest,valor):
    Est = Estudiante.objects.get(idest=idest)
    idcurso = str(Est.idcur.codigo)
    messages.success(request, 'asistencia registrada')
    Asist = ListaAsistencias.objects.create(idestAsist=Est,valorAsist=valor)
    return redirect('/est/Registro/'+str(idcurso))
