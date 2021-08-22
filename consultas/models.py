from django.db import models
from pacientes.models import Pacientes
from medicos.models import Medicos

class Consultas(models.Model):
  paciente = models.ForeignKey(Pacientes, on_delete=models.PROTECT)
  medico = models.ForeignKey(Medicos, on_delete=models.PROTECT)
  data = models.DateTimeField()
  valor = models.CharField(max_length=20)
  convenio = models.CharField(max_length=40)

  def __str__(self):
    return self.convenio
