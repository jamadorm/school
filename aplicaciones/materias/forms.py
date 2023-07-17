from django.forms import ModelForm

from aplicaciones.materias.models import Materia


class MateriaForm(ModelForm):
    class Meta:
        model = Materia
        fields = '__all__'
        widgets = {

        }
