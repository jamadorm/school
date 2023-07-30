from django.db import models


# Create your models here.

class TipoSangre(models.Model):
    tipo_sangre = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.tipo_sangre


class CicloEscolar(models.Model):
    ciclo_escolar = models.CharField(max_length=50)
    comentarios = models.TextField()

    def __str__(self):
        return self.ciclo_escolar


class Sexo(models.Model):
    sexo = models.CharField(max_length=15)

    def __str__(self):
        return self.sexo


class Grado(models.Model):
    grado = models.CharField(max_length=50)
    subgrado = models.CharField(max_length=20, null=True)
    comentarios = models.CharField(null=True, default="Sin comentarios.")

    def __str__(self):
        return self.grado, self.subgrado


