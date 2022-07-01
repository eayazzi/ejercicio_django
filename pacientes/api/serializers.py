from rest_framework import serializers
from rest_framework.views import APIView

from pacientes.models import Paciente
from datetime import date

class  PacienteSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
        
    def get_full_name(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name) 

    class Meta:
        model = Paciente
        fields = ['first_name', 'last_name', 'full_name', 'age', 
                'dni','date_of_birth','phone', 'social_work', 'location', 'address']
        extra_kwargs = {
            'first_name': {'write_only': True},
            'last_name': {'write_only': True},
            'date_of_birth': {'write_only': True},
            'social_work': {'write_only': True},
            'location': {'write_only': True},
            'address': {'write_only': True},
        }

    
    