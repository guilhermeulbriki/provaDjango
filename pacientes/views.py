from django.shortcuts import render
from .models import Pacientes
from consultas.models import Consultas

def index(request):
  pacientes = Pacientes.objects.all()
  return render(request, 'pacientes.html', {'pacientes':pacientes})


def infoPacientes(request, id):
  paciente = Pacientes.objects.get(id=id)
  consultas = Consultas.objects.all().filter(paciente=id)
  return render(request, 'infoPacientes.html', {'paciente':paciente, 'consultas':consultas})
