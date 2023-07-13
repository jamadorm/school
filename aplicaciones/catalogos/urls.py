from django.urls import path

from aplicaciones.catalogos.views import inicio, ListadoCiclos, NuevoCicloEscolar, EdicionCiclo, ActualizarCiclo, \
    EliminarCiclo

urlpatterns = [
    path('', inicio, name='inicio'),
    path('listado_ciclos', ListadoCiclos, name="listado_ciclos"),
    path('nuevo_ciclo', NuevoCicloEscolar, name="NuevoCicloEscolar"),
    path('eliminar_ciclo/<id>', EliminarCiclo, name="eliminar_ciclo"),
    path('edicion_ciclo/<id>', EdicionCiclo, name="edicion_ciclo"),
    path('actualizar_ciclo/', ActualizarCiclo, name="actualizar_ciclo"),
]
