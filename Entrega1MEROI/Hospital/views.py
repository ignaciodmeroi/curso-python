from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


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