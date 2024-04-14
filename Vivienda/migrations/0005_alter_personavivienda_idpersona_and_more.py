# Generated by Django 5.0.3 on 2024-04-14 17:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Persona', '0003_delete_tipovivienda_remove_persona_idvivienda_and_more'),
        ('Vivienda', '0004_personavivienda_propietario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personavivienda',
            name='idPersona',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Persona.persona'),
        ),
        migrations.AlterField(
            model_name='personavivienda',
            name='idVivienda',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Vivienda.vivienda'),
        ),
    ]