# Generated by Django 3.2.13 on 2023-02-26 16:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Estudiantes', '0002_listaasistencias'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listaasistencias',
            name='fecha',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]