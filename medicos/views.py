from django.shortcuts import render
from .models import Medicos
from consultas.models import Consultas

def index(request):
  medicos = Medicos.objects.all()
  return render(request, 'medicos.html', {'medicos':medicos})


def infoMedicos(request, id):
  medico = Medicos.objects.get(id=id)
  consultas = Consultas.objects.all().filter(medico=id)
  return render(request, 'infoMedicos.html', {'medico':medico, 'consultas':consultas})