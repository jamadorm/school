from django.forms import ModelForm

from aplicaciones.alumnos.models import Alumno, AlumnoTutores


class AlumnoForm(ModelForm):
    class Meta:
        model = Alumno
        fields = '__all__'
        widgets = {
        }


class AlumnoTutorForm(ModelForm):
    class Meta:
        model = AlumnoTutores
        fields = '__all__'
        widgets = {

        }
