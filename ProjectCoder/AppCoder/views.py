from django.http import HttpResponse
from django.shortcuts import render
from AppCoder import views
from AppCoder.models import Curso
from django.template import loader

# Create your views here.
def inicio (request):
    return render(request, 'AppCoder/inicio.html')

def cursos(self):
    docuemnto= f"Pagina de cursos"
    return HttpResponse(docuemnto)

def profesores(self):
    docuemnto= f"Pagina de profesores"
    return HttpResponse(docuemnto)

def estudiantes(self):
    docuemnto= f"Pagina de estudiantes"
    return HttpResponse(docuemnto)

def entregables(self):
    docuemnto= f"Pagina de entregables"
    return HttpResponse(docuemnto)




