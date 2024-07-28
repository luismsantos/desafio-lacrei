from django.test import TestCase
from .models import Medico, Consulta, Paciente
from django.utils.html import escape
import datetime

class PacienteModelTest(TestCase):
    
    def setUp(self):
        self.paciente = Paciente.objects.create(
            nomeCompleto = 'Luisa',
            nomeSocial = 'Luisa',
            endereco = 'Rua das margaridas',
            idade = 30
        )
    
    def test_paciente_creation(self):
        self.assertIsInstance(self.paciente, Paciente)
        self.assertEqual(self.paciente.nomeCompleto, 'Luisa')
        self.assertEqual(self.paciente.nomeSocial, 'Luisa')
        self.assertEqual(self.paciente.endereco, 'Rua das margaridas')
        self.assertEqual(self.paciente.idade, 30)
        

    def test_paciente_str(self):
      self.assertEqual(str(self.paciente), f' Paciente: {escape(self.paciente.nomeSocial)}')



class MedicoModelTest(TestCase):
    
    def setUp(self):
        self.medico = Medico.objects.create(
            nomeCompleto = 'Rales',
            nomeSocial = 'Tales',
            profissao = 'Psicologo',
            endereco = 'Mercadao',
            idade = 23
      )
        
    def test_medico_creation(self):
        self.assertIsInstance(self.medico, Medico)
        self.assertEqual(self.medico.nomeCompleto, 'Rales')
        self.assertEqual(self.medico.nomeSocial, 'Tales')
        self.assertEqual(self.medico.profissao, 'Psicologo')
        self.assertEqual(self.medico.endereco, 'Mercadao')
        self.assertEqual(self.medico.idade, 23)
        

    def test_medico_str(self):
      self.assertEqual(str(self.medico), f' Médico: {escape(self.medico.nomeSocial)}')



class ConsultaModelTest(TestCase):
    
    def setUp(self):
        self.paciente = Paciente.objects.create(
            nomeCompleto = 'Luisa',
            nomeSocial = 'Luisa',
            endereco = 'Rua das margaridas',
            idade = 30
        )

        self.medico = Medico.objects.create(
            nomeCompleto = 'Rales',
            nomeSocial = 'Tales',
            profissao = 'Psicologo',
            endereco = 'Mercadao',
            idade = 23
         )   
        
        self.consulta = Consulta.objects.create(
            medico=self.medico,
            paciente=self.paciente,
            dataConsulta=datetime.date.today()
        )

    def test_consulta_creation(self):
        self.assertIsInstance(self.consulta, Consulta)
        self.assertEqual(self.consulta.medico, self.medico)
        self.assertEqual(self.consulta.paciente, self.paciente)
        self.assertEqual(self.consulta.dataConsulta, datetime.date.today())

    def test_consulta_str(self):
        self.assertEqual(str(self.consulta), f'{escape(self.medico.nomeSocial)} - {escape(self.paciente.nomeSocial)}')

        
  