from django.urls import path,include
from . import views
from ..Estudiantes import urls

urlpatterns = [
    path('', views.home),
    path('registrarCurso/', views.registrarCurso),
    path('edicionCurso/<codigo>', views.edicionCurso),
    path('editarCurso/', views.editarCurso),
<<<<<<< HEAD
    path('eliminarCurso/<codigo>', views.eliminarCurso)
=======
    path('eliminarCurso/<codigo>', views.eliminarCurso),
    path('ListaEstCurso/<codigo>',include(urls))
>>>>>>> 7963514e59fe1158b073527349fd15b8e4aad62f
]