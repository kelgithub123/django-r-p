from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeEst),
    path('est/<codigo>', views.ListaEstCurso),
    path('edicionEst/<codigo>', views.edicionEst),
    path('registrarEst/', views.registrarEst),
    path('editarEst/<idest>', views.editarEst),
    path('eliminarEst/<codigo>', views.eliminarEst)
]