from django.db import models

from aplicaciones.catalogos.models import Sexo, TipoSangre


# Create your models here.

class Maestro(models.Model):
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
    foto_perfil = models.ImageField(upload_to="alumnos/", verbose_name="foto_perfil", null=True, default="sin_foto.png", blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    user_name = models.CharField(max_length=20)
    password_user = models.CharField(max_length=50)
    # ultima_modificacion = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.nombre+" "+self.apellido_paterno+" "+self.apellido_materno