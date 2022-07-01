from django.db import models
from datetime import date
from django.core.validators import MaxValueValidator, MinValueValidator

class Paciente(models.Model):
    first_name = models.CharField(max_length=150, verbose_name="Nombre")
    last_name = models.CharField(max_length=150, verbose_name="Apellido")
    dni = models.PositiveIntegerField(validators=[MaxValueValidator(99999999), MinValueValidator(5000)])
    date_of_birth = models.DateTimeField(verbose_name="Fecha de Nacimiento")
    phone = models.CharField(max_length=50, null=True, blank=True, verbose_name="Telefono")
    social_work = models.CharField(max_length=150, verbose_name="Obra Social")
    location = models.CharField(max_length=150, null=True, blank=True, verbose_name="Localidad")
    address = models.CharField(max_length=150, verbose_name="Dirección")

    def age(self):
        return date.today().year - self.date_of_birth.year

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'