from django.urls import path

from aplicaciones.catalogos.views import inicio, ListadoCiclos, NuevoCicloEscolar, EdicionCiclo, ActualizarCiclo, \
    EliminarCiclo, NuevoGrado, ListadoGrados, EdicionGrado, ActualizarGrado, EliminarGrado, NuevoGrupo, ListadoGrupo, \
    EdicionGrupo, ActualizarGrupo, EliminarGrupo

urlpatterns = [
    path('', inicio, name='inicio'),
    # CATÁLOGO CICLO ESCOLAR
    path('listado_ciclos', ListadoCiclos, name="listado_ciclos"),
    path('nuevo_ciclo', NuevoCicloEscolar, name="NuevoCicloEscolar"),
    path('eliminar_ciclo/<id>', EliminarCiclo, name="eliminar_ciclo"),
    path('edicion_ciclo/<id>', EdicionCiclo, name="edicion_ciclo"),
    path('actualizar_ciclo/', ActualizarCiclo, name="actualizar_ciclo"),

    # CATÁLOGO GRADO
    path('nuevo_grado/', NuevoGrado, name="nuevo_grado"),
    path('listado_grados', ListadoGrados, name="listado_grados"),
    path('edicion_grado/<id>', EdicionGrado, name="edicion_grado"),
    path('actualizar_grado', ActualizarGrado, name="actualizar_grado"),
    path('eliminar_grado/<id>', EliminarGrado, name="eliminar_grado"),

    # CATÁLOGO GRUPO
    path('nuevo_grupo/', NuevoGrupo, name="nuevo_grupo"),
    path('listado_grupos', ListadoGrupo, name="listado_grupos"),
    path('edicion_grupo/<id>', EdicionGrupo, name="edicion_grupoo"),
    path('actualizar_grupo', ActualizarGrupo, name="actualizar_grupo"),
    path('eliminar_grupo/<id>', EliminarGrupo, name="eliminar_grupo"),
]
