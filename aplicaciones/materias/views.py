from django.contrib import messages
from django.shortcuts import render, redirect

from aplicaciones.catalogos.models import CicloEscolar, Grado
from aplicaciones.maestros.models import Maestro
from aplicaciones.materias.forms import MateriaForm
from aplicaciones.materias.models import Materia


# Create your views here.
def NuevaMateria(request):
    if request.method == 'POST':
        formularioMateria = MateriaForm(request.POST, request.FILES)
        if formularioMateria.is_valid():
            formularioMateria.save()
            messages.success(request, "new")
            return redirect('listado_materias')
        else:
            print("ERROR - No se pudo grabar el formulario")
            messages.success(request, "error")
            return redirect('listado_materias')
    else:
        ciclos_escolares = CicloEscolar.objects.all()
        maestros = Maestro.objects.all()
        grados = Grado.objects.all()
        formularioMateria = MateriaForm()
        return render(request, 'nueva_materia.html',
                      {'formularioMateria': formularioMateria, 'ciclos_escolares': ciclos_escolares,
                       'maestros': maestros, 'grados': grados})


def ListadoMaterias(request):
    materias = Materia.objects.all()
    return render(request, 'listado_materias.html', {'materias': materias})


def EditarMateria(request, id):
    materia = Materia.objects.get(id=id)
    grados = Grado.objects.all()
    ciclos_escolares = CicloEscolar.objects.all()
    maestros = Maestro.objects.all()
    return render(request, 'editar_materia.html', {'materia': materia, 'ciclos_escolares': ciclos_escolares, 'maestros': maestros, 'grados': grados})


def EdicionMateria(request):
    if request.method == 'POST':
        id_materia = request.POST['id_materia']
        materia = Materia.objects.get(id=id_materia)
        formularioMateria = MateriaForm(request.POST, request.FILES, instance=materia)
        if formularioMateria.is_valid():
            formularioMateria.save()
            messages.success(request, 'edit')
            return redirect('listado_materias')
        else:
            print("El formulario es inválido")
    else:
        materia = Materia.objects.get(id=id)
        ciclos_escolares = CicloEscolar.objects.all()
        maestros = Maestro.objects.all()
        return render(request, 'editar_materia.html',
                      {'materia': materia, 'ciclos_escolares': ciclos_escolares, 'maestros': maestros})


def EliminarMateria(request, id):
    materia = Materia.objects.get(id=id)
    materia.delete()
    messages.success(request, 'delete')
    return redirect('listado_materias')


def BuscarMateria(request):
    if request.method == 'GET':
        print(request)
        if 'id' in request.GET:
            print("Si existe variable")
            id_materia = request.GET['id']
            materia = Materia.objects.get(id=id_materia)
            return render(request, 'perfil_materia.html', {'materia': materia})
        else:
            print("NO existe variable")
            materias = Materia.objects.all()
            return render(request, 'buscar_materia.html', {'materias': materias})
    else:
        if request.method == 'POST':
            id_materia = request.POST['materia']
            materia = Materia.objects.get(id=id_materia)
            return render(request, 'perfil_materia.html', {'materia': materia})
        else:
            materias = Materia.objects.all()
            return render(request, 'buscar_materia.html', {'materias': materias})
