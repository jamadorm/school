# Generated by Django 4.2.2 on 2023-08-01 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0009_grupo_remove_grado_subgrado_gradogrupo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gradogrupo',
            name='id_grado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogos.grado', unique=True),
        ),
        migrations.AlterField(
            model_name='gradogrupo',
            name='id_grupo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogos.grupo', unique=True),
        ),
    ]
