from django.urls import path
from AppCoder.views import inicio, cursos, profesores, estudiantes, entregables, cursoFormulario, profesorFormulario, busquedaCamada, busqueda, leerProfesores, eliminarProfesor


urlpatterns = [
    path('', inicio, name='Inicio'),
    path('cursos', cursos, name='Cursos'),
    path('estudiantes', estudiantes, name='Estudiantes'),
    path('entregables', entregables, name='Entregables'),
    path('formulario', cursoFormulario, name='CursoFormulario'),
    path('profeform', profesorFormulario,name='ProfeFormulario'),
    path('busquedacamada', busquedaCamada,name='BusquedaCamada'),
    path('busqueda', busqueda, name='Busqueda'),
    path('profesores', leerProfesores, name='Profesores'),
    path('eliminarProfesor/<nombre>', eliminarProfesor, name='EliminarProfesor')
]