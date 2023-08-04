from django.db import models

from aplicaciones.catalogos.models import Sexo, TipoSangre
from aplicaciones.tutores.models import Tutor


# Create your models here.

class Alumno(models.Model):
    nombre = models.CharField(max_length=80)
    apellido_paterno = models.CharField(max_length=40)
    apellido_materno = models.CharField(max_length=40)
    fecha_nacimiento = models.DateField()
    curp = models.CharField(max_length=18)
    id_sexo = models.ForeignKey(Sexo, on_delete=models.CASCADE)
    email = models.EmailField(max_length=50)
    telefono = models.CharField(max_length=15)
    tipo_sangre = models.ForeignKey(TipoSangre, on_delete=models.CASCADE)
    domicilio = models.TextField()
    foto_perfil = models.ImageField(upload_to="alumnos/", verbose_name="foto_perfil", null=True, default="sin_foto.png",
                                    blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    # ultima_modificacion = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.nombre + " " + self.apellido_paterno + " " + self.apellido_materno


class AlumnoTutores(models.Model):
    id_alumno = models.ForeignKey(Alumno, on_delete=models.SET_NULL, null=True)
    id_tutor = models.ForeignKey(Tutor, on_delete=models.SET_NULL, null=True)
    parentesco = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.id_alumno.__str__()+" / "+ self.id_tutor.__str__()
