# Generated by Django 4.2.2 on 2023-06-14 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutores', '0004_tutor_foto_perfil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutor',
            name='foto_perfil',
            field=models.ImageField(default='sin_foto.png', null=True, upload_to='tutores/', verbose_name='foto_perfil'),
        ),
    ]
