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
        return render(request, 'nueva_materia.html', {'formularioMateria': formularioMateria, 'ciclos_escolares': ciclos_escolares, 'maestros': maestros})


def ListadoMaterias(request):
    materias = Materia.objects.all()
    print(materias)
    return render(request, 'listado_materias.html', {'materias': materias})

def EditarMaterias(request, id):
    return
