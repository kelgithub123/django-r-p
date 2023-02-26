from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeEst),
<<<<<<< HEAD
    path('<codigo>', views.homeEst),
    path('listaCurso/<codigo>', views.ListaEstCurso),
    path('edicionEst/<codigo>', views.edicionEst),
    path('registrarEst/', views.registrarEst),
    path('editarEst/<idest>', views.editarEst),
    path('eliminarEst/<codigo>', views.eliminarEst)
=======
    path('edicionEst/', views.edicionEst),
    path('edicionEst/<codigo>', views.edicionEst),
    path('ListaEstCurso/<codigo>', views.ListaEstCurso),
    path('registrarEst/', views.registrarEst),
    path('editarEst/<idest>', views.editarEst),
    path('eliminarEst/<codigo>', views.eliminarEst),
>>>>>>> 7963514e59fe1158b073527349fd15b8e4aad62f
]