from django.urls import path

from aplicaciones.maestros.views import InicioMaestro, ListadoMaestros, NuevoMaestro, EdicionMaestro, EditarMaestro, \
    EliminarMaestro, BuscarMaestro, PerfilMaestro

urlpatterns = [
    path('', InicioMaestro, name='inicio_maestro'),
    path('listado_maestros', ListadoMaestros, name="listado_maestros"),
    path('nuevo_maestro', NuevoMaestro, name="nuevo_maestro"),
    path('edicion_maestro/<id>', EdicionMaestro, name="edicion_maestro"),
    path('editar_maestro', EditarMaestro, name="editar_maestro"),
    path('buscar_maestro', BuscarMaestro, name="buscar_maestro"),
    path('buscar_maestro/<id>', BuscarMaestro, name="buscar_maestro"),
    path('perfil_maestro', PerfilMaestro, name="perfil_maestro"),
    path('eliminar_maestro/<id>', EliminarMaestro, name="eliminar_maestro"),
]