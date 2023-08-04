from django.contrib import admin

from aplicaciones.alumnos.models import Alumno, AlumnoTutores

# Register your models here.
admin.site.register(Alumno)
admin.site.register(AlumnoTutores)