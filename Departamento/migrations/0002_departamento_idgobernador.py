# Generated by Django 5.0.3 on 2024-04-12 04:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Departamento', '0001_initial'),
        ('Persona', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='departamento',
            name='idGobernador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Persona.persona'),
        ),
    ]
