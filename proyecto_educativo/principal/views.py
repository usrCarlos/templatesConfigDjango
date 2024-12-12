from django.shortcuts import render, get_object_or_404
from .models import Estudiantes

# Create your views here.

def home(request):
    estudiantes = Estudiantes.objects.all()
    return render(request, 'index.html', {'estudiantes': estudiantes})

def detalle_estudiante(request, estudiante_id):
    estudiante = get_object_or_404(Estudiantes, pk = estudiante_id)
    return render(request, 'detalle.html', {'estudiante' : estudiante}) 