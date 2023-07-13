from django.shortcuts import render, redirect

from .forms import CicloForm
from .models import CicloEscolar
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
