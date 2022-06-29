from django.http import HttpResponse
from django.shortcuts import render
from AppCoder import views
from AppCoder.models import Curso, Profesor, Estudiantes
from django.template import loader
from AppCoder.forms import CursoFormulario, ProfesorFormulario
from django.views.generic.detail import DetailView
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy 
# Create your views here.
def inicio (self):
    plantilla = loader.get_template('AppCoder/inicio.html')
    documento = plantilla.render()
    return HttpResponse(documento)

def cursos(request):
    return render(request, 'AppCoder/cursos.html')

def profesores(request):
    return render(request, 'AppCoder/profesores.html')

def estudiantes(request):
    return render(request, 'AppCoder/estudiantes.html')

def entregables(request):
    return render(request, 'AppCoder/entregables.html')

def cursoFormulario(request):
    if request.method == 'POST':
        miFormulario = CursoFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            nombre = informacion['nombre']
            camada = informacion['camada']
            curso = Curso(nombre=nombre, camada=camada)
            curso.save()
            return render(request, 'AppCoder/inicio.html')
    else:
        miFormulario = CursoFormulario()

    return render(request, 'AppCoder/cursoFormulario.html', {"miFormulario":miFormulario})


def busquedaCamada(request):
    return render(request, 'AppCoder/busquedaCamada.html')

def busqueda(request):
    # respuesta = f"Estoy buscando la comision {request.GET['camada']}"
    if request.GET['camada']:
        camada = request.GET['camada']
        cursos = Curso.objects.filter(camada=camada)
        return render(request, 'AppCoder/resultadosBusqueda.html', {'cursos': cursos, 'camada': camada})
    else:
        respuesta = "No se ha ingresado ninguna comision"
    return HttpResponse(respuesta)


#CRUD read profesores
def leerProfesores(request):
    profesores = Profesor.objects.all()   
    contexto = {'profesores': profesores}
    

    return render(request, "AppCoder/profesores.html", contexto)

#CRUD create profesores
def profesorFormulario(request):
    if request.method == 'POST':
        miFormulario = ProfesorFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            info = miFormulario.cleaned_data
            nombre = info['nombre']
            apellido = info['apellido']
            email = info['email']
            profesion = info['profesion']
            profe = Profesor(nombre=nombre, apellido=apellido, email=email, profesion= profesion)
            profe.save()
            return render(request, 'AppCoder/inicio.html')
    else:
        miFormulario = ProfesorFormulario()

    return render(request, 'AppCoder/profesorFormulario.html', {"miFormulario":miFormulario})

#CRUD delete profesores
def eliminarProfesor(request, nombre):
    profesor = Profesor.objects.get(nombre=nombre)
    profesor.delete()

    profesores = Profesor.objects.all()
    contexto = {'profesores':profesores}
    return render(request, 'AppCoder/profesores.html', contexto)

#CRUD update profesores
def editarProfesor(request, profesor_nombre):
    profesor = Profesor.objects.get(nombre=profesor_nombre)

    if request.method == 'POST':
        miFormulario = ProfesorFormulario(request.POST)
        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            profesor.nombre = informacion['nombre']
            profesor.apellido = informacion['apellido']
            profesor.email = informacion['email']
            profesor.profesion = informacion['profesion']

            profesor.save()

            profesores = Profesor.objects.all()
            contexto = {'profesores': profesores}
            return render(request,'AppCoder/profesores.html', contexto)
    else: 
        miFormulario = ProfesorFormulario(initial={'nombre':profesor.nombre, 'apellido':profesor.apellido, 'email':profesor.email, 'profesion':profesor.profesion})
        contexto = {'miFormulario': miFormulario, 'profesor_nombre': profesor_nombre}
        return render(request, 'AppCoder/editarProfesor.html', contexto)

#----------------------------------------------------------------
#LISTVIEW
class EstudiantesList(ListView):
    model = Estudiantes
    template_name = 'AppCoder/estudiantes.html'

#DETAILVIEW 
class EstudianteDetail(DetailView):
    model = Estudiantes 
    template_name = 'AppCoder/estudiante_detalle.html'

class EstudianteCreacion(CreateView):
    model = Estudiantes 
    success_url = reverse_lazy('Estudiante_list')
    fields = ['nombre', 'apellido', 'email']

class EstudianteEdicion(UpdateView):
    model = Estudiantes 
    success_url = reverse_lazy('Estudiante_list')
    fields = ['nombre', 'apellido', 'email']

class EstudianteEliminacion(DeleteView):
    model = Estudiantes 
    success_url = reverse_lazy('Estudiante_list')