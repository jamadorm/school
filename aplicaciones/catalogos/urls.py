from django.urls import path

from aplicaciones.catalogos.views import inicio, ListadoCiclos, NuevoCicloEscolar, EdicionCiclo, ActualizarCiclo, \
    EliminarCiclo, NuevoGrado, ListadoGrados, EdicionGrado, ActualizarGrado, EliminarGrado

urlpatterns = [
    path('', inicio, name='inicio'),
    path('listado_ciclos', ListadoCiclos, name="listado_ciclos"),
    path('nuevo_ciclo', NuevoCicloEscolar, name="NuevoCicloEscolar"),
    path('eliminar_ciclo/<id>', EliminarCiclo, name="eliminar_ciclo"),
    path('edicion_ciclo/<id>', EdicionCiclo, name="edicion_ciclo"),
    path('actualizar_ciclo/', ActualizarCiclo, name="actualizar_ciclo"),
    path('nuevo_grado_escolar/', NuevoGrado, name="nuevo_grado_escolar"),
    path('listado_grados', ListadoGrados, name="listado_grados"),
    path('edicion_grado/<id>', EdicionGrado, name="edicion_grado"),
    path('actualizar_grado', ActualizarGrado, name="actualizar_grado"),
    path('eliminar_grado/<id>', EliminarGrado, name="eliminar_grado"),

]
