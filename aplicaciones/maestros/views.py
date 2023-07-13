from django.contrib import messages
from django.shortcuts import render, redirect

from aplicaciones.catalogos.models import Sexo, TipoSangre
from aplicaciones.maestros.forms import MaestroForm
from aplicaciones.maestros.models import Maestro


# Create your views here.

def InicioMaestro(request):
    return render(request, "inicio_maestros.html")


def ListadoMaestros(request):
    maestros = Maestro.objects.all()
    return render(request, 'listado_maestros.html', {"maestros": maestros})


def NuevoMaestro(request):
    if request.method == 'POST':
        formularioMaestro = MaestroForm(request.POST, request.FILES)
        if formularioMaestro.is_valid():
            formularioMaestro.save()
            messages.success(request, "new")
            return redirect('listado_maestros')
        else:
            print("ERROR - No se pudo grabar el formulario")
    else:
        formularioMaestro = MaestroForm()
        cat_sexo = Sexo.objects.all()
        cat_tipo_sangre = TipoSangre.objects.all()
        return render(request, 'nuevo_maestro.html', {"formularioMaestro": formularioMaestro, "cat_sexo": cat_sexo,
                                                      "cat_tipo_sangre": cat_tipo_sangre})


def EdicionMaestro(request, id):
    maestro = Maestro.objects.get(id=id)
    cat_sexo = Sexo.objects.all()
    cat_tipo_sangre = TipoSangre.objects.all()
    return render(request, 'edicion_maestro.html',
                  {"maestro": maestro, "cat_sexo": cat_sexo, "cat_tipo_sangre": cat_tipo_sangre})


def EditarMaestro(request):
    if request.method == 'POST':
        id = request.POST['id']
        maestro = Maestro.objects.get(id=id)
        formulariomaestro = MaestroForm(request.POST, request.FILES, instance=maestro)
        if formulariomaestro.is_valid():
            formulariomaestro.save()
            messages.success(request, 'edit')
            return redirect('listado_maestros')
        else:
            print("El formulario es inválido")
    else:
        maestro = Maestro.objects.get(id=id)
        cat_sexo = Sexo.objects.all()
        cat_tipo_sangre = TipoSangre.objects.all()
        return render(request, 'edicion_maestro.html',
                      {"maestro": maestro, "cat_sexo": cat_sexo, "cat_tipo_sangre": cat_tipo_sangre})


def EliminarMaestro(request, id):
    maestro = Maestro.objects.get(id=id)
    maestro.delete()
    messages.success(request, 'delete')
    return redirect('listado_maestros')


def BuscarMaestro(request):
    if request.method == 'POST':
        id_maestro = request.POST['maestro']
        maestro = Maestro.objects.get(id=id_maestro)
        return render(request, 'perfil_maestro.html', {"maestro": maestro})
    else:
        maestros = Maestro.objects.all()
        return render(request, 'buscar_maestro.html', {"maestros": maestros})


def PerfilMaestro(request):
    return render(request, 'perfil_maestro.html')
