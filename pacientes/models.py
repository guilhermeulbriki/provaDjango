from django.db import models

class Pacientes(models.Model):
  nome = models.CharField(max_length=100)
  cpf = models.CharField(max_length=14)
  email = models.CharField(max_length=100)
  telefone = models.CharField(max_length=15)
  idade = models.IntegerField()
  endereco = models.TextField()

  def __str__(self):
    return self.nome
