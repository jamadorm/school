from django.urls import path

from aplicaciones.materias.views import NuevaMateria, ListadoMaterias, EditarMateria, EdicionMateria, BuscarMateria

urlpatterns = [
    path('nueva_materia', NuevaMateria, name="nueva_materia"),
    path('listado_materias', ListadoMaterias, name="listado_materias"),
    path('editar_materia/<id>', EditarMateria, name="editar_materia"),
    path('edicion_materia', EdicionMateria, name="edicion_materia"),
    path('buscar_materia',BuscarMateria, name="buscar_materia"),


]