from django.urls import path,include
from . import views
from ..Estudiantes import urls

urlpatterns = [
    path('', views.home),
    path('registrarCurso/', views.registrarCurso),
    path('edicionCurso/<codigo>', views.edicionCurso),
    path('editarCurso/', views.editarCurso),
    path('eliminarCurso/<codigo>', views.eliminarCurso),
    path('est/<codigo>',include('Aplicaciones.Estudiantes.urls'))
]