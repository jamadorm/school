from django.urls import path

from aplicaciones.catalogos.views import inicio, ListadoCiclos, NuevoCicloEscolar, EdicionCiclo, ActualizarCiclo, \
    EliminarCiclo
from aplicaciones.grados_escolares.views import NuevoGrupoEscolar, ListadoGradoGrupo, PreAsignarAlumnos, AsignacionAlumnos, BuscarGrupoEscolar, ListarAlumnos

urlpatterns = [
    path('listado_grado_grupo_escolar', ListadoGradoGrupo, name="listado_grado_grupo_escolar"),
    path('nuevo_grupo_escolar', NuevoGrupoEscolar, name="nuevo_grupo_escolar"),
    path('asignar_alumnos/<id>', PreAsignarAlumnos, name="asignar_alumnos"),
    path('listar_alumnos/<id>', ListarAlumnos, name="listar_alumnos"),
    path('asignacion_alumnos', AsignacionAlumnos, name="asignacion_alumnos"),
    path('buscar_grupo_escolar', BuscarGrupoEscolar, name="buscar_grupo_escolar"),


    path('eliminar_ciclo/<id>', EliminarCiclo, name="eliminar_ciclo"),
    path('edicion_ciclo/<id>', EdicionCiclo, name="edicion_ciclo"),
    path('actualizar_ciclo/', ActualizarCiclo, name="actualizar_ciclo"),


]