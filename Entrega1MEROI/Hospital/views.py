from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from Hospital.forms import PacienteFormulario, ProfesionalFormulario, AsistenteFormulario


# Create your views here.
def inicio (self):
    plantilla = loader.get_template('Hospital/inicio.html')
    documento = plantilla.render()
    return HttpResponse(documento)

def paciente(request):
    return render(request, 'Hospital/paciente.html')

def profesional(request):
    return render(request, 'Hospital/profesional.html')

def asistente(request):
    return render(request, 'Hospital/asistente.html')

#----------------------------------------------------------------
# FORMULARIOS:

def pacienteFormulario(request):
    if request.method == 'POST':
        miFormulario = PacienteFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            nombre = informacion['nombre']
            apellido = informacion['apellido']
            dni = informacion['dni']
            email = informacion['email']
            paciente = paciente(nombre=nombre, apellido=apellido, dni = dni, email=email)
            paciente.save()
            return render(request, 'Hospital/inicio.html')
    else:
        miFormulario = PacienteFormulario()

    return render(request, 'Hospital/pacienteFormulario.html', {"miFormulario":miFormulario})

def profesionalFormulario(request):
    if request.method == 'POST':
        miFormulario = ProfesionalFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            nombre = informacion['nombre']
            apellido = informacion['apellido']
            especialidad = informacion['especialidad']
            matricula = informacion['matricula']
            email = informacion['email']
            paciente = paciente(nombre=nombre, apellido=apellido, especialidad = especialidad, matricula = matricula ,email=email)
            paciente.save()
            return render(request, 'Hospital/inicio.html')
    else:
        miFormulario = ProfesionalFormulario()

    return render(request, 'Hospital/profesionalFormulario.html', {"miFormulario":miFormulario})

def asistenteFormulario(request):
    if request.method == 'POST':
        miFormulario = AsistenteFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            nombre = informacion['nombre']
            apellido = informacion['apellido']
            nempleado = informacion['nempleado']
            email = informacion['email']
            paciente = paciente(nombre=nombre, apellido=apellido, nempleado = nempleado ,email=email)
            paciente.save()
            return render(request, 'Hospital/inicio.html')
    else:
        miFormulario = AsistenteFormulario()

    return render(request, 'Hospital/asistenteFormulario.html', {"miFormulario":miFormulario})