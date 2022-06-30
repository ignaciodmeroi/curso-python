from django.urls import path
from AppCoder.views import inicio, cursos, profesores, estudiantes, entregables, cursoFormulario, profesorFormulario, busquedaCamada, busqueda, leerProfesores, eliminarProfesor, editarProfesor, login_request, register_request
from AppCoder.views import EstudianteDetail, EstudianteCreacion, EstudianteEdicion, EstudianteEliminacion, EstudiantesList




urlpatterns = [
    path('', inicio, name='Inicio'),
    path('cursos', cursos, name='Cursos'),
    path('estudiantes', estudiantes, name='Estudiantes'),
    path('entregables', entregables, name='Entregables'),
    path('formulario', cursoFormulario, name='CursoFormulario'),
    path('profeform', profesorFormulario,name='ProfeFormulario'),
    path('busquedacamada', busquedaCamada,name='BusquedaCamada'),
    path('busqueda', busqueda, name='Busqueda'),
    #---------------------------------
    path('profesores', leerProfesores, name='Profesores'),
    path('eliminarProfesor/<nombre>', eliminarProfesor, name='EliminarProfesor'),
    path('editarProfesor/<profesor_nombre>', editarProfesor, name='EditarProfesor'),
    #--------------------------------
    path('estudiante/list/', EstudiantesList.as_view(), name='Estudiante_list'),
    path('estudiante/<pk>', EstudianteDetail.as_view(), name='Estudiante_detalle'),
    path('estudiante/nuevo/', EstudianteCreacion.as_view(), name='Estudiante_crear'),
    path('estudiante/edicion/<pk>', EstudianteEdicion.as_view(), name='Estudiante_edicion'),
    path('estudiante/borrar/<pk>', EstudianteEliminacion.as_view(), name='Estudiante_borrar'),
    #------------------------------
    #Login
    path('login', login_request, name='login'),
    path('register', register_request, name='registro'),
]