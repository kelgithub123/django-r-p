from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeEst),
    path('<codigo>', views.homeEst),
    path('listaCurso/<codigo>', views.ListaEstCurso),
    path('edicionEst/<codigo>', views.edicionEst),
    path('registrarEst/', views.registrarEst),
    path('editarEst/<idest>', views.editarEst),
    path('Registro/<curso>', views.registro),
    path('Actividad/<id>', views.mostraractividad),
    path('registrarAct/<curso>', views.registrarActividad),
    path('registrarNota/', views.registrarnota),
    path('listaDeAsistencia/<curso>', views.verlistaAsistencia),
    path('Asistencia/<idest>/<valor>/<curso>', views.registrarAsist),
    path('eliminarEst/<codigo>', views.eliminarEst)
]