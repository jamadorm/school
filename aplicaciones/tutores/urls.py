from django.urls import path

from aplicaciones.tutores.views import inicio, ListadoTutores, NuevoTutor, EliminarTutor, EdicionTutor, EditarTutor


urlpatterns = [
    path('', inicio, name='inicio_tutores'),
    path('listado_tutores', ListadoTutores, name="listado_tutores"),
    path('nuevo_tutor', NuevoTutor, name="nuevo_tutor"),
    path('edicion_tutor/<id>', EdicionTutor, name="edicion_tutor"),
    path('editar_tutor/', EditarTutor, name="editar_tutor"),
    path('eliminar_tutor/<id>', EliminarTutor, name="eliminar_tutor"),

]