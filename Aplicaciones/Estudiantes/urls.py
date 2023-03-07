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
    path('Asistencia/<idest>/<valor>', views.registrarAsist),
    path('eliminarEst/<codigo>', views.eliminarEst)
]