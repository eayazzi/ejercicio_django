from django.contrib import admin

from pacientes.models import Paciente

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    ordering = ['id']
    search_fields = ['last_name']
    list_display = ['first_name', 'last_name', 'dni']
