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
    actividadeslist=Actividades.objects.all()
    Listaest = []
    if not Asistencias:
        Listaest=EstudListados 
        return render(request, "RegistroEst.html",{"Estudiantes": Listaest,"Asistentes":Asistencias,"curso":curso,"actividades":actividadeslist})
    else:
        for est in EstudListados:
            sw=0
            id=est.idest
            for estAsist in Asistencias:
                if estAsist.idestAsist.idest == id:
                    sw=1
            if sw == 0:                       
                Listaest.append(est) 
        return render(request, "RegistroEst.html",{"Estudiantes": Listaest,"Asistentes":Asistencias,"curso":curso,"actividades":actividadeslist})    

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
    messages.success(request, 'registradO!!')
    Asist = ListaAsistencias.objects.create(idestAsist=Est,valorAsist=valor)
    return redirect('/est/Registro/'+str(idcurso))

def registrarActividad(request,curso):
    nombre = request.POST['Nombre']
    consigna = request.POST['consigna']
    fecha = request.POST['fecha']
    Actividad = Actividades.objects.create(nombreAct=nombre, fechaAct=fecha, consignaAct=consigna)
    messages.success(request, '¡Actividad registrada!')
    return redirect('/est/Registro/'+str(curso))

def mostraractividad(request,id):    
    fecha=datetime.date.today()
    Actividad = Actividades.objects.get(idact=id)
    actividadeslist=Actividades.objects.all()
    calificados=Notas.objects.exclude(idactNota=id)
    Asistentes=ListaAsistencias.objects.filter(fechaAsist=fecha,valorAsist=1)
    return render(request,'actividadesEst.html',{"actSel":Actividad,"Asistentes":Asistentes,"actividades":actividadeslist})

def registrarnota(request):
    nota = request.POST['nota']
    estudiante = Estudiante.objects.get(idest=request.POST['idest'])
    actividad = Actividades.objects.get(idact=request.POST['idact'])
    Nota = Notas.objects.create(valorNota=nota,idestNota=estudiante,idActNota=actividad)
    messages.success(request, 'nota registrada!')
    return redirect('/est/Actividad/'+str(actividad.idact))