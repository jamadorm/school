import psycopg2
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect

from aplicaciones.alumnos.conex.conex import conexion
from aplicaciones.alumnos.models import Alumno
from aplicaciones.catalogos.models import Grado, Grupo
from aplicaciones.grados_escolares.forms import GradoGrupoForm, GradoGrupoAlumnosForm
from aplicaciones.grados_escolares.models import GradoGrupo, GradoGrupoAlumnos


# Create your views here.
def NuevoGrupoEscolar(request):
    if request.method == 'POST':
        gradogrupoFormulario = GradoGrupoForm(request.POST)
        if gradogrupoFormulario.is_valid():
            gradogrupoFormulario.save()
            messages.success(request, 'new')
            return redirect('listado_grado_grupo_escolar')
        else:
            print("Formulario inválido...NuevoGrupoEscolar")
            messages.success(request, 'error')
            return redirect('listado_grado_grupo_escolar')
    grados = Grado.objects.all()
    grupos = Grupo.objects.all()
    gradogrupoFormulario = GradoGrupoForm()
    return render(request, 'nuevo_grado_grupo.html',
                  {'grados': grados, 'grupos': grupos, 'gradogrupoFormulario': gradogrupoFormulario})


def ListadoGradoGrupo(request):
    gradogrupos = GradoGrupo.objects.all()
    return render(request, 'listado_grado_grupo.html', {'gradogrupos': gradogrupos})


def PreAsignarAlumnos(request, id):
    id_grado_grupo = GradoGrupo.objects.get(id=id)
    alumnos = Alumno.objects.all()
    formGradoGrupo = GradoGrupoAlumnosForm()
    return render(request, 'asignar_alumnos.html',
                  {'id_grado_grupo': id_grado_grupo, 'alumnos': alumnos, 'formGradoGrupo': formGradoGrupo})


def AsignacionAlumnos(request):
    if request.method == 'POST':
        id_grado_grupo = request.POST['id_grado_grupo']
        id_alumnos = request.POST.getlist("id_alumno[]")
        print("id_grado_grupo: ", id_grado_grupo)
        print("id_alumnos: ", id_alumnos)
        try:
            cursor = conexion.cursor()
            for id_alumno in id_alumnos:
                print("id_grado_grupo:" + id_grado_grupo + " - id_alumno: " + id_alumno)
                consulta = "INSERT INTO grados_escolares_gradogrupoalumnos (id_alumno_id, id_grado_grupo_id) VALUES (" \
                           "%s::bigint, %s::bigint)"
                cursor.execute(consulta, (id_alumno, id_grado_grupo))
            conexion.commit()

        except psycopg2.Error as e:
            print("Ocurrió un error al insertar: ", e)
        finally:
            conexion.close()
        return redirect('listado_grado_grupo_escolar')
    else:
        return redirect('listado_grado_grupo_escolar')


def BuscarGrupoEscolar(request):
    return HttpResponse("Saludos")


def ListarAlumnos(request, id):
    listado_alumnos = GradoGrupoAlumnos.objects.filter(id_grado_grupo_id=id)
    print(listado_alumnos)
    return render(request, 'listado_grado_grupo_alumnos.html', {'listado_alumnos': listado_alumnos})
