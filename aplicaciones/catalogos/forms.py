from django.forms import ModelForm, TextInput

from aplicaciones.catalogos.models import CicloEscolar


class CicloForm(ModelForm):
    class Meta:
        model = CicloEscolar
        fields = '__all__'
        widgets = {
            'nombre': TextInput(attrs={'class': 'form-control'}),
            'apellido_paterno': TextInput(attrs={'class': 'form-control'}),
        }
