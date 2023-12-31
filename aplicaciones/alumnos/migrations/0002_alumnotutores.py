# Generated by Django 4.2.2 on 2023-06-22 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tutores', '0006_alter_tutor_foto_perfil'),
        ('alumnos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlumnoTutores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_alumno', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='alumnos.alumno')),
                ('id_tutor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tutores.tutor')),
            ],
        ),
    ]
