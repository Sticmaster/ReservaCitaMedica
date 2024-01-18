# myapp/tests/test_models.py
from django.test import TestCase
from .models import Paciente, Medico, Reserva
from .serializers import PacienteSerializer, MedicoSerializer, ReservaSerializer

class PacienteModelTest(TestCase):

    def test_paciente_creation(self):
        paciente = Paciente.objects.create(
            nombre='John',
            apellido='Doe',
            edad=30,
            foto_perfil='profile.jpg',
            correo='john.doe@example.com',
            medicamento='Aspirin',
            alergia='None',
            actividad='Running'
        )
        self.assertEqual(paciente.nombre, 'John')


class MedicoModelTest(TestCase):

    def test_medico_creation(self):
        medico = Medico.objects.create(
            nombre='Dr. Smith',
            apellido='Johnson',
            edad=45,
            foto_perfil='doctor.jpg',
            telefono='123-456-7890',
            especialidad='Cardiologist',
            categoria='Senior',
            actividad='Consulting'
        )
        self.assertEqual(medico.nombre, 'Dr. Smith')


class ReservaModelTest(TestCase):

    def test_reserva_creation(self):
        paciente = Paciente.objects.create(
            nombre='John',
            apellido='Doe',
            edad=30,
            foto_perfil='profile.jpg',
            correo='john.doe@example.com',
            medicamento='Aspirin',
            alergia='None',
            actividad='Running'
        )

        medico = Medico.objects.create(
            nombre='Dr. Smith',
            apellido='Johnson',
            edad=45,
            foto_perfil='doctor.jpg',
            telefono='123-456-7890',
            especialidad='Cardiologist',
            categoria='Senior',
            actividad='Consulting'
        )

        reserva = Reserva.objects.create(
            descripcion='Checkup',
            fecha='2024-01-18',
            hora='08:30:00',
            costo=50,
            estado='Pending',
            idPaciente=paciente,
            idMedico=medico
        )
        self.assertEqual(reserva.descripcion, 'Checkup')


class PacienteSerializerTest(TestCase):

    def test_paciente_serializer_with_valid_data(self):
        data = {
            'nombre': 'John',
            'apellido': 'Doe',
            'edad': 30,
            'foto_perfil': 'profile.jpg',
            'correo': 'john.doe@example.com',
            'medicamento': 'Aspirin',
            'alergia': 'None',
            'actividad': 'Running'
        }
        serializer = PacienteSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_paciente_serializer_with_invalid_data(self):
        data = {
            'nombre': 'John',
            'apellido': 'Doe',
            'edad': 'invalid_age', 
            'foto_perfil': 'profile.jpg',
            'correo': 'john.doe@example.com',
            'medicamento': 'Aspirin',
            'alergia': 'None',
            'actividad': 'Running'
        }
        serializer = PacienteSerializer(data=data)
        self.assertFalse(serializer.is_valid())


class MedicoSerializerTest(TestCase):

    def test_medico_serializer_with_valid_data(self):
        data = {
            'nombre': 'Dr. Smith',
            'apellido': 'Johnson',
            'edad': 45,
            'foto_perfil': 'doctor.jpg',
            'telefono': '123-456-7890',
            'especialidad': 'Cardiologist',
            'categoria': 'Senior',
            'actividad': 'Consulting'
        }
        serializer = MedicoSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_medico_serializer_with_invalid_data(self):
        data = {
            'nombre': 'Dr. Smith',
            'apellido': 'Johnson',
            'edad': 'invalid_age',  
            'foto_perfil': 'doctor.jpg',
            'telefono': '123-456-7890',
            'especialidad': 'Cardiologist',
            'categoria': 'Senior',
            'actividad': 'Consulting'
        }
        serializer = MedicoSerializer(data=data)
        self.assertFalse(serializer.is_valid())

class ReservaSerializerTest(TestCase):

    def test_reserva_serializer_with_valid_data(self):
        paciente = Paciente.objects.create(
            nombre='John',
            apellido='Doe',
            edad=30,
            foto_perfil='profile.jpg',
            correo='john.doe@example.com',
            medicamento='Aspirin',
            alergia='None',
            actividad='Running'
        )

        medico = Medico.objects.create(
            nombre='Dr. Smith',
            apellido='Johnson',
            edad=45,
            foto_perfil='doctor.jpg',
            telefono='123-456-7890',
            especialidad='Cardiologist',
            categoria='Senior',
            actividad='Consulting'
        )

        data = {
            'descripcion': 'Checkup',
            'fecha': '2024-01-18',
            'hora': '08:30:00',
            'costo': 50,
            'estado': 'Pending',
            'idPaciente': paciente.pk,
            'idMedico': medico.pk
        }
        serializer = ReservaSerializer(data=data)
        self.assertTrue(serializer.is_valid())