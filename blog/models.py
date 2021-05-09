from django.contrib.auth.models import User
from django.db import models


class Agente(models.Model):
    nombre = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.nombre.username


class Secretaria(models.Model):
    nombre = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.nombre.username


class Citas(models.Model):
    identificacion = models.IntegerField('PID', unique = True, blank = False)
    superficie = models.CharField('Superficie', max_length=50, blank=False)
    dormitorios = models.IntegerField('Dormitorios', blank=False)
    baños = models.IntegerField('Baños', blank=False)
    precio = models.DecimalField('Precio', max_digits = 16, decimal_places = 2)
    nombre_apellido = models.CharField('Nombre cliente', max_length=100, blank=False)
    num_cliente = models.IntegerField('Cel./Tel.')
    email = models.EmailField('Email', blank = True, null = True)
    propiedad = models.CharField('Propiedad', max_length=50, blank=False)
    fecha_cita = models.DateField('Fecha de cita', blank = True, null=True)
    hora_cita = models.TimeField('Hora de cita', blank=True, null=True)    
    agente = models.ForeignKey(Agente, on_delete = models.CASCADE, blank=True, null=True)
    estado_cita = models.BooleanField('Atendido/a', blank=True, null=True)


    class Meta:
        verbose_name = "Cita"
        verbose_name_plural = "Citas"


    def __str__(self):
        pid = str(self.identificacion)
        return pid