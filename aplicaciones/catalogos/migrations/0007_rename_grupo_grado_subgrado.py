# Generated by Django 4.2.2 on 2023-07-25 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0006_delete_grupo_grado_grupo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='grado',
            old_name='grupo',
            new_name='subgrado',
        ),
    ]