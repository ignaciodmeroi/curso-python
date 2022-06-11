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
    path('busquedaPaciente', busquedaPaciente,name='BusquedaPaciente'),
    path('busqueda', busqueda, name='Busqueda'),
]