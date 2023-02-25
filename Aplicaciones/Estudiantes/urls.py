from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeEst),
    path('edicionEst/', views.edicionEst),
    path('edicionEst/<codigo>', views.edicionEst),
    path('ListaEstCurso/<codigo>', views.ListaEstCurso),
    path('registrarEst/', views.registrarEst),
    path('editarEst/<idest>', views.editarEst),
    path('eliminarEst/<codigo>', views.eliminarEst),
]