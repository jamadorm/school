from django.forms import ModelForm

from aplicaciones.grados_escolares.models import GradoGrupo


class GradoGrupoForm(ModelForm):
    class Meta:
        model = GradoGrupo
        fields = '__all__'
        widgets = {}