from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend

from pacientes.models import Paciente
from pacientes.api.serializers import PacienteSerializer

class PacienteApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PacienteSerializer
    pagination_class = PageNumberPagination
    queryset = Paciente.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['last_name', 'dni']