from django.forms import ModelForm

from aplicaciones.tutores.models import Tutor


class TutorForm(ModelForm):
    class Meta:
        model = Tutor
        fields = '__all__'
        widgets = {
        }