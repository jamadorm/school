# Generated by Django 4.2.2 on 2023-07-25 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0007_rename_grupo_grado_subgrado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grado',
            name='comentarios',
            field=models.CharField(default='Sin comentarios.', null=True),
        ),
    ]
