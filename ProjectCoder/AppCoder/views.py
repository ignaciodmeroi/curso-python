from django.http import HttpResponse
from django.shortcuts import render

from AppCoder.models import Curso

# Create your views here.
def curso(request):

    return render(request, 'familia.html')  