from django.contrib import admin

from aplicaciones.catalogos.models import CicloEscolar, Sexo, TipoSangre

# Register your models here.
admin.site.register(CicloEscolar)
admin.site.register(Sexo)
admin.site.register(TipoSangre)
