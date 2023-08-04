from django.forms import ModelForm, TextInput

from aplicaciones.catalogos.models import CicloEscolar, Grado, Grupo


class CicloForm(ModelForm):
    class Meta:
        model = CicloEscolar
        fields = '__all__'
        widgets = {
            'nombre': TextInput(attrs={'class': 'form-control'}),
            'apellido_paterno': TextInput(attrs={'class': 'form-control'}),
        }


class GradoForm(ModelForm):
    class Meta:
        model = Grado
        fields = '__all__'
        widgets = {}


class GrupoForm(ModelForm):
    class Meta:
        model = Grupo
        fields = '__all__'
        widgets = {}