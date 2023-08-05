from django.forms import ModelForm

from aplicaciones.grados_escolares.models import GradoGrupo, GradoGrupoAlumnos


class GradoGrupoForm(ModelForm):
    class Meta:
        model = GradoGrupo
        fields = '__all__'
        widgets = {}


class GradoGrupoAlumnosForm(ModelForm):
    class Meta:
        model = GradoGrupoAlumnos
        fields = '__all__'
        widgets = {}