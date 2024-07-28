from django.db import models
from django.utils.html import escape
import uuid

class Medico(models.Model):
  id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
  nomeCompleto = models.CharField(max_length=255)
  nomeSocial= models.CharField(max_length=255)
  profissao = models.CharField(max_length=100)
  endereco= models.CharField(max_length=255)
  idade = models.IntegerField()

  def __str__(self):
    return f' Médico: {escape(self.nomeSocial)}'
  

class Paciente(models.Model):
  id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
  nomeCompleto = models.CharField(max_length=255)
  nomeSocial = models.CharField(max_length=255)
  endereco = models.CharField(max_length=255)
  idade= models.IntegerField()

  def __str__ (self):
    return f' Paciente: {escape(self.nomeSocial)}'

class Consulta(models.Model):
  id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
  medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
  paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
  dataConsulta = models.DateField()



  def __str__(self):
    return f'{escape(self.medico.nomeSocial)} - {escape(self.paciente.nomeSocial)}'

  