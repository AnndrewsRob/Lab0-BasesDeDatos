# Generated by Django 5.0.3 on 2024-04-12 06:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Departamento', '0002_departamento_idgobernador'),
        ('Municipio', '0001_initial'),
        ('Persona', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='municipio',
            old_name='nombre',
            new_name='nombreMunicipio',
        ),
        migrations.AddField(
            model_name='municipio',
            name='area',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='municipio',
            name='idAlcalde',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Persona.persona'),
        ),
        migrations.AddField(
            model_name='municipio',
            name='idDepartamento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Departamento.departamento'),
        ),
        migrations.AddField(
            model_name='municipio',
            name='presupuesto',
            field=models.FloatField(blank=True, null=True),
        ),
    ]