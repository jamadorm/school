from django.contrib import messages
from django.shortcuts import render, redirect

from aplicaciones.catalogos.models import CicloEscolar
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
    else:
        ciclos_escolares = CicloEscolar.objects.all()
        maestros = Maestro.objects.all()
        formularioMateria = MateriaForm()
        return render(request, 'nueva_materia.html',
                      {'formularioMateria': formularioMateria, 'ciclos_escolares': ciclos_escolares,
                       'maestros': maestros})


def ListadoMaterias(request):
    materias = Materia.objects.all()
    return render(request, 'listado_materias.html', {'materias': materias})


def EditarMateria(request, id):
    materia = Materia.objects.get(id=id)
    ciclos_escolares = CicloEscolar.objects.all()
    maestros = Maestro.objects.all()
    return render(request, 'editar_materia.html', {'materia': materia, 'ciclos_escolares': ciclos_escolares, 'maestros': maestros})


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


def BuscarMateria(request):
    materias = Materia.objects.all()
    return render(request, 'buscar_materia.html', {'materias': materias})
