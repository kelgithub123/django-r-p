# Generated by Django 4.1.6 on 2023-03-11 11:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Estudiantes', '0021_merge_20230311_0724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listaasistencias',
            name='fechaAsist',
            field=models.DateField(default=datetime.date(2023, 3, 11)),
        ),
    ]
