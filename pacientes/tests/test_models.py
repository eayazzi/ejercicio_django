from django.test import TestCase
from pacientes.models import Paciente


class ModelsTestCase(TestCase):
    def setUp(self):
        self.instance = Paciente(
            first_name='Epi',
            last_name='Ayazzi',
            dni=34819346,
            date_of_birth='01-01-2021 00:00',
            phone='3415504867',
            social_work='Omint',
            location='Rosario',
            address='Jujuy 2323',
        )

    def test_save(self):
        self.instance.save
        self.assertEquals(self.instance.first_name, 'Epi')