# Generated by Django 3.2.13 on 2022-06-29 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0003_auto_20220629_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='address',
            field=models.CharField(max_length=150, verbose_name='Dirección'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='date_of_birth',
            field=models.DateTimeField(verbose_name='Fecha de Nacimiento'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='first_name',
            field=models.CharField(max_length=150, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='last_name',
            field=models.CharField(max_length=150, verbose_name='Apellido'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='location',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Localidad'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='phone',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Telefono'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='social_work',
            field=models.CharField(max_length=150, verbose_name='Obra Social'),
        ),
    ]
