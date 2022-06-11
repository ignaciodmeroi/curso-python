from django.urls import path
from Hospital.views import inicio, paciente, profesional, asistente, pacienteFormulario, asistenteFormulario, profesionalFormulario, busqueda, busquedaPaciente


urlpatterns = [
    path('', inicio, name='Inicio'),
    path('paciente', paciente, name='Paciente'),
    path('profesional', profesional, name='Profesional'),
    path('asistente', asistente, name='Asistente'),
    path('pacienteFormulario', pacienteFormulario, name='PacienteFormulario'),
    path('profesionalFormulario', profesionalFormulario, name='ProfesionalFormulario'),
    path('asistenteFormulario', asistenteFormulario, name='AsistenteFormulario'),
    path('busquedapaciente', busquedaPaciente,name='BusquedaPaciente'),
    path('busqueda', busqueda, name='Busqueda'),
    #path('profeform', profesorFormulario,name='ProfeFormulario'),
    #path('busquedacamada', busquedaCamada,name='BusquedaCamada'),
    #path('busqueda', busqueda, name='Busqueda'),
    #path('profesores', leerProfesores, name='Profesores'),
    #path('eliminarProfesor/<nombre>', eliminarProfesor, name='EliminarProfesor'),
    #path('editarProfesor/<profesor_nombre>', editarProfesor, name='EditarProfesor'),
    #--------------------------------
    #path('estudiante/list/', EstudiantesList.as_view(), name='Estudiante_list'),
    #path('estudiante/<pk>', EstudianteDetail.as_view(), name='Estudiante_detalle'),
    #path('estudiante/nuevo/', EstudianteCreacion.as_view(), name='Estudiante_crear'),
    #path('estudiante/edicion/<pk>', EstudianteEdicion.as_view(), name='Estudiante_edicion'),
    #path('estudiante/borrar/<pk>', EstudianteEliminacion.as_view(), name='Estudiante_borrar'),
]