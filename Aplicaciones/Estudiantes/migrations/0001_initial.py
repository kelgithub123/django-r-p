# Generated by Django 3.2.13 on 2023-02-25 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Cursos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('idest', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('paterno', models.CharField(max_length=20)),
                ('materno', models.CharField(max_length=20)),
                ('idcur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cursos.curso')),
            ],
        ),
    ]
