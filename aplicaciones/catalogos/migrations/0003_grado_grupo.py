# Generated by Django 4.2.2 on 2023-07-23 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0002_tiposangre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grado', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grupo', models.CharField(max_length=30)),
            ],
        ),
    ]
