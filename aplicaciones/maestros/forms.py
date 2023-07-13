from django.forms import ModelForm

from aplicaciones.maestros.models import Maestro


class MaestroForm(ModelForm):
    class Meta:
        model = Maestro
        fields = '__all__'
        widgets = {

        }
