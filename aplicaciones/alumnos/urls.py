from django.urls import path

from aplicaciones.alumnos.views import InicioAlumno, ListadoAlumnos, NuevoAlumno, EliminarAlumno, EdicionAlumno, \
    EditarAlumno, PerfilAlumno, BuscarAlumno, PerfilAlumnoBuscado, TutorAlumno, DetallesTutor, Pruebas, TutoresAsignados

urlpatterns = [
    path('', InicioAlumno, name='inicio_alumnos'),
    path('listado_alumnos', ListadoAlumnos, name='listado_alumnos'),
    path('nuevo_alumno', NuevoAlumno, name='nuevo_alumno'),
    path('edicion_alumno/<id>', EdicionAlumno, name='edicion_alumno'),
    path('editar_alumno', EditarAlumno, name='editar_alumno'),
    path('eliminar_alumno/<id>', EliminarAlumno, name='eliminar_alumno'),
    path('perfil_alumno/<id>', PerfilAlumno, name='perfil_alumno'),
    path('buscar_alumno', BuscarAlumno, name='buscar_alumno'),
    path('perfil_alumno_buscado', PerfilAlumnoBuscado, name='perfil_alumno_buscado'),
    path('tutor_alumno', TutorAlumno, name='tutor_alumno'),
    path('tutores_asignados', TutoresAsignados, name='tutores_asignados'),
    path('detalles_tutor', DetallesTutor, name='detalles_tutor'),
    path('borrar', Pruebas, name='borrar'),

]
