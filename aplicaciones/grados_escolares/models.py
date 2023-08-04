from django.db import models

from aplicaciones.alumnos.models import Alumno
from aplicaciones.catalogos.models import Grado, Grupo
from aplicaciones.maestros.models import Maestro


# Create your models here.
class GradoGrupo(models.Model):
    id_grado = models.ForeignKey(Grado, on_delete=models.DO_NOTHING)
    id_grupo = models.ForeignKey(Grupo, on_delete=models.DO_NOTHING)
    comentarios = models.CharField(null=True, default="Sin comentarios.")

    def __str__(self):
        return self.id_grado.__str__() + " - " + self.id_grupo.__str__()

    def presentacion(self):
        return "Grado: " + self.id_grado.__str__() + " | Grupo: " + self.id_grupo.__str__()


class GradoGrupoAlumnos(models.Model):
    id_grado_grupo = models.ForeignKey(GradoGrupo, on_delete=models.DO_NOTHING)
    id_alumno = models.ForeignKey(Alumno, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.id_grado_grupo.__str__() + " / " + self.id_alumno.__str__()


class GradoGrupoMaestros(models.Model):
    id_grado_grupo = models.ForeignKey(GradoGrupo, on_delete=models.DO_NOTHING)
    id_maestro = models.ForeignKey(Maestro, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.id_grado_grupo.__str__() + " / " + self.id_maestro.__str__()
