# Generated by Django 4.2.2 on 2023-08-01 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0011_alter_gradogrupo_id_grado_alter_gradogrupo_id_grupo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='GradoGrupo',
        ),
    ]
