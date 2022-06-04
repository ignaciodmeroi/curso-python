from django.http import HttpResponse
from django.shortcuts import render
from AppCoder import views
from AppCoder.models import Curso

# Create your views here.
def inicio(request):
     return render(request, 'AppCoder/inicio.html')

def cursos(request):
    return render(request, 'AppCoder/curso.html')

def profesores(request):
    return render(request, 'AppCoder/profesores.html')

def estudiantes(request):
    return render(request, 'AppCoder/estudiantes.html')

def entregables(request):
    return render(request, 'AppCoder/entregables.html')