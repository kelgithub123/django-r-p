# Generated by Django 4.1.6 on 2023-03-07 22:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Estudiantes', '0019_alter_listaasistencias_fechaasist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listaasistencias',
            name='fechaAsist',
            field=models.DateField(default=datetime.date(2023, 3, 7)),
        ),
    ]