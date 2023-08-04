from django.contrib import admin

from aplicaciones.catalogos.models import CicloEscolar, Sexo, TipoSangre, Grado, Grupo

# Register your models here.
admin.site.register(CicloEscolar)
admin.site.register(Sexo)
admin.site.register(TipoSangre)
admin.site.register(Grado)
admin.site.register(Grupo)

