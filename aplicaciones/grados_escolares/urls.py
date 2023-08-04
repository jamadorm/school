from django.urls import path

from aplicaciones.catalogos.views import inicio, ListadoCiclos, NuevoCicloEscolar, EdicionCiclo, ActualizarCiclo, \
    EliminarCiclo
from aplicaciones.grados_escolares.views import NuevoGrupoEscolar, ListadoGradoGrupo, AsignarAlumnos

urlpatterns = [
    path('listado_grado_grupo_escolar', ListadoGradoGrupo, name="listado_grado_grupo_escolar"),
    path('nuevo_grupo_escolar', NuevoGrupoEscolar, name="nuevo_grupo_escolar"),
    path('asignar_alumnos/<id>', AsignarAlumnos, name="asignar_alumnos"),


    path('eliminar_ciclo/<id>', EliminarCiclo, name="eliminar_ciclo"),
    path('edicion_ciclo/<id>', EdicionCiclo, name="edicion_ciclo"),
    path('actualizar_ciclo/', ActualizarCiclo, name="actualizar_ciclo"),


]