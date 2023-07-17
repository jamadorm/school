from django.urls import path

from aplicaciones.materias.views import NuevaMateria, ListadoMaterias, EditarMaterias

urlpatterns = [
    path('nueva_materia', NuevaMateria, name="nueva_materia"),
    path('listado_materias', ListadoMaterias, name="listado_materias"),
    path('editar_materia/<id>', EditarMaterias, name="editar_materia"),


]