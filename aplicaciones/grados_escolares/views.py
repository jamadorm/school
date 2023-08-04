from django.contrib import messages
from django.shortcuts import render, redirect

from aplicaciones.alumnos.models import Alumno
from aplicaciones.catalogos.models import Grado, Grupo
from aplicaciones.grados_escolares.forms import GradoGrupoForm
from aplicaciones.grados_escolares.models import GradoGrupo


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
    return render(request, 'nuevo_grado_grupo.html', {'grados': grados, 'grupos': grupos, 'gradogrupoFormulario': gradogrupoFormulario})


def ListadoGradoGrupo(request):
    gradogrupos = GradoGrupo.objects.all()
    return render(request,'listado_grado_grupo.html', {'gradogrupos': gradogrupos})


def AsignarAlumnos(request, id):
    id_grado_grupo = GradoGrupo.objects.get(id=id)
    alumnos = Alumno.objects.all()
    return render(request, 'asignar_alumnos.html', {'id_grado_grupo': id_grado_grupo, 'alumnos': alumnos})