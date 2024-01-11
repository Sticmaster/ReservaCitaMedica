from django.db import models

# Create your models here.
class Paciente(models.Model):
    idPaciente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length = 25)
    apellido = models.CharField(max_length = 25)
    edad = models.PositiveSmallIntegerField()
    foto_perfil = models.CharField(max_length = 100)
    correo = models.EmailField((""), max_length=254)
    medicamento = models.CharField(max_length = 50)
    alergia = models.CharField(max_length = 50)
    actividad = models.CharField(max_length = 100)

    def __str__(self):
      return self.nombre

class Medico(models.Model):
    idMedico = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length = 25)
    apellido = models.CharField(max_length = 25)
    edad = models.PositiveSmallIntegerField()
    foto_perfil = models.CharField(max_length = 100)
    telefono = models.CharField(max_length = 100)
    especialidad = models.CharField(max_length = 50)
    categoria = models.CharField(max_length = 50)
    actividad = models.CharField(max_length = 100)

    def __str__(self):
      return self.nombre

class Reserva(models.Model):
    descripcion = models.CharField(max_length = 100)
    fecha = fecha = models.DateField()
    hora = models.TimeField()
    costo = models.PositiveSmallIntegerField()
    estado = models.CharField(max_length = 20)
    idPaciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    idMedico = models.ForeignKey(Medico, on_delete=models.CASCADE)
