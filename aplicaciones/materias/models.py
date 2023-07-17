from django.db import models

from aplicaciones.catalogos.models import CicloEscolar
from aplicaciones.maestros.models import Maestro


# Create your models here.
class Materia(models.Model):
    materia = models.CharField(max_length=100)
    codigo_materia = models.CharField(max_length=20)
    detalles_materia = models.TextField(null=True)
    id_ciclo_escolar = models.ForeignKey(CicloEscolar, on_delete=models.CASCADE)
    id_maestro = models.ForeignKey(Maestro, on_delete=models.CASCADE)
    foto_libro = models.ImageField(upload_to="materias/", verbose_name="foto_libro", null=True, default="sin_foto_libro.png", blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

