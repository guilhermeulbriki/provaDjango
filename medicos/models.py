from django.db import models

class Medicos(models.Model):
  nome = models.CharField(max_length=100)
  cpf = models.CharField(max_length=14)
  email = models.CharField(max_length=100)
  telefone = models.CharField(max_length=15)
  crm = models.CharField(max_length=20)
  especialidade = models.CharField(max_length=100)

  def __str__(self):
    return self.nome
