# Generated by Django 3.2.13 on 2023-02-26 16:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Estudiantes', '0006_remove_listaasistencias_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='listaasistencias',
            name='fecha',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]