from django.shortcuts import render, redirect

from .forms import CicloForm, GradoForm, GrupoForm
from .models import CicloEscolar, Grado, Grupo
from django.contrib import messages


# Create your views here.

def inicio(request):
    return render(request, "inicio.html")


def ListadoCiclos(request):
    ciclo_escolar = CicloEscolar.objects.all()
    messages.success(request, 'lista_ciclos')
    return render(request, "listado_ciclo_escolar.html", {"CicloEscolar": ciclo_escolar})


def NuevoCicloEscolar(request):
    if request.method == 'POST':
        formularioCiclo = CicloForm(request.POST)
        if formularioCiclo.is_valid():
            formularioCiclo.save()
            messages.success(request, 'new')
        return redirect('listado_ciclos')
    else:
        formularioCiclo = CicloForm()
    return render(request, "nuevo_ciclo.html", {"formularioCiclo": formularioCiclo})


def EliminarCiclo(request, id):
    ciclo = CicloEscolar.objects.get(id=id)
    ciclo.delete()
    messages.success(request, 'delete')
    return redirect('listado_ciclos')


def EdicionCiclo(request, id):
    ciclo = CicloEscolar.objects.get(id=id)
    return render(request, "editar_ciclo.html", {"ciclo": ciclo})


def ActualizarCiclo(request):
    id = request.POST['id']
    ciclo = CicloEscolar.objects.get(id=id)
    if request.method == 'POST':
        formularioCiclo = CicloForm(request.POST, instance=ciclo)
        if formularioCiclo.is_valid():
            formularioCiclo.save()
            messages.success(request, 'edit')
        return redirect('listado_ciclos')
    else:
        return render(request, "listado_ciclo_escolar.html")

# views GRADO
def NuevoGrado(request):
    if request.method == 'POST':
        gradoFormulario = GradoForm(request.POST)
        if gradoFormulario.is_valid():
            gradoFormulario.save()
            messages.success(request, 'new')
            return redirect('listado_grados')
        else:
            messages.success(request, 'error')
            return redirect('listado_grados')
    else:
        gradoFormulario = GradoForm()
        return render(request, 'grado/nuevo_grado.html', {'gradoFormulario': gradoFormulario})


def ListadoGrados(request):
    grados = Grado.objects.all()
    return render(request, 'grado/listado_grado.html', {'grados': grados})


def EdicionGrado(request, id):
    grado = Grado.objects.get(id=id)
    return render(request, 'grado/editar_grado.html', {'grado': grado})


def ActualizarGrado(request):
    if request.method == 'POST':
        id_grado = request.POST['id']
        print('id_grado= ' + id_grado)
        grado = Grado.objects.get(id=id_grado)
        gradoForm = GradoForm(request.POST, instance=grado)
        if gradoForm.is_valid():
            gradoForm.save()
            messages.success(request, 'edit')
            return redirect('listado_grados')
        else:
            print('Formulario inválido')
            messages.success(request, 'error')
            return redirect('listado_grados')
    else:
        print('Formulario inválido')
        messages.success(request, 'error')
        return redirect('listado_grados')


def EliminarGrado(request, id):
    grado = Grado.objects.get(id=id)
    grado.delete()
    messages.success(request, 'delete')
    return redirect('listado_grados')


# views GRUPO
def NuevoGrupo(request):
    if request.method == 'POST':
        grupoFormulario = GrupoForm(request.POST)
        if grupoFormulario.is_valid():
            grupoFormulario.save()
            messages.success(request, 'new')
            return redirect('listado_grupos')
        else:
            messages.success(request, 'error')
            return redirect('listado_grupos')
    else:
        grupoFormulario = GrupoForm()
        return render(request, 'grupos/nuevo_grupo.html', {'grupoFormulario': grupoFormulario})


def ListadoGrupo(request):
    grupos = Grupo.objects.all()
    return render(request, 'grupos/listado_grupo.html', {'grupos': grupos})


def EdicionGrupo(request, id):
    grupo = Grupo.objects.get(id=id)
    return render(request, 'grupos/editar_grupo.html', {'grupo': grupo})





def ActualizarGrupo(request):
    if request.method == 'POST':
        id_grupo = request.POST['id']
        print('id_grupo= ' + id_grupo)
        grupo = Grupo.objects.get(id=id_grupo)
        grupoForm = GrupoForm(request.POST, instance=grupo)
        if grupoForm.is_valid():
            grupoForm.save()
            messages.success(request, 'edit')
            return redirect('listado_grupos')
        else:
            print('Formulario inválido')
            messages.success(request, 'error')
            return redirect('listado_grupos')
    else:
        print('Formulario inválido')
        messages.success(request, 'error')
        return redirect('listado_grupos')


def EliminarGrupo(request, id):
    grupo = Grupo.objects.get(id=id)
    grupo.delete()
    messages.success(request, 'delete')
    return redirect('listado_grupos')
