# Generated by Django 4.2.2 on 2023-06-28 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0002_alumnotutores'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumnotutores',
            name='parentesco',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
