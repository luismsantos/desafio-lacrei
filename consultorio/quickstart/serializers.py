from rest_framework import serializers
from .models import Medico, Paciente, Consulta

class MedicoSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Medico
    fields = ('id', 'nomeCompleto' ,'nomeSocial', 'profissao', 'endereco', 'idade')
    
class PacienteSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Paciente
    fields = ('id', 'nomeCompleto', 'nomeSocial', 'endereco', 'idade')
    
class ConsultaSerializer(serializers.ModelSerializer):

  idMedico = serializers.PrimaryKeyRelatedField(queryset=Medico.objects.all(), source='medico', write_only=True)
  nomeMedico = serializers.CharField(source='medico.nomeSocial', read_only=True)
  idPaciente = serializers.PrimaryKeyRelatedField(queryset=Paciente.objects.all(), source='paciente', write_only=True)
  nomePaciente = serializers.CharField(source='paciente.nomeSocial', read_only=True)
 

  class Meta:
    model = Consulta
    fields = ('id', 'idMedico', 'nomeMedico', 'idPaciente', 'nomePaciente', 'dataConsulta')
