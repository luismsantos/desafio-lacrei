from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Medico, Paciente, Consulta
from .serializers import MedicoSerializer, PacienteSerializer, ConsultaSerializer

class MedicoViewSet(viewsets.ModelViewSet):
  queryset = Medico.objects.all()
  serializer_class = MedicoSerializer


  def delete(self, request):
        itm = Medico.objects.get(pk=request.DATA.get('pk'))
        itm.delete()
        return Response({
            'success': True,
            'level'  : 'success',
            'message': ("Deletado"),
        })

class PacienteViewSet(viewsets.ModelViewSet):
  queryset = Paciente.objects.all()
  serializer_class = PacienteSerializer

  def delete(self, request):
        itm = Paciente.objects.get(pk=request.DATA.get('pk'))
        itm.delete()
        return Response({
            'success': True,
            'level'  : 'success',
            'message': ("Deletado"),
        })

class ConsultaViewSet(viewsets.ModelViewSet):
  queryset = Consulta.objects.all()
  serializer_class = ConsultaSerializer

  def delete(self, request):
        itm = Consulta.objects.get(pk=request.DATA.get('pk'))
        itm.delete()
        return Response({
            'success': True,
            'level'  : 'success',
            'message': ("Deletado"),
        })



