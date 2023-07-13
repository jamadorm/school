from django.shortcuts import render, redirect

from django.contrib import messages

from aplicaciones.catalogos.models import Sexo, TipoSangre
from aplicaciones.tutores.forms import TutorForm
from aplicaciones.tutores.models import Tutor


# Create your views here.

def inicio(request):
    return render(request, "inicio_tutores.html")


def ListadoTutores(request):
    listado_tutores = Tutor.objects.all()
    messages.success(request, 'lista_tutores')
    return render(request, "listado_tutores.html", {"tutores": listado_tutores})


def NuevoTutor(request):
    cat_sexo = Sexo.objects.all()
    cat_tipo_sangre = TipoSangre.objects.all()
    if request.method == 'POST':
        formularioTutor = TutorForm(request.POST, request.FILES)
        if formularioTutor.is_valid():
            formularioTutor.save()
            messages.success(request, 'new')
            return redirect('listado_tutores')
        else:
            print("Formulario no Válido. No se pudo guardar")
    else:
        formularioTutor = TutorForm()
    return render(request, "nuevo_tutor.html", {"formularioTutor": formularioTutor, "cat_sexo": cat_sexo, "cat_tipo_sangre": cat_tipo_sangre})


def EdicionTutor_2(request, id):
    tutor = Tutor.objects.get(id=id)
    formularioTutor = TutorForm(instance=tutor)
    return render(request, "edicion_tutor.html", {"formularioTutor": formularioTutor})


def EdicionTutor(request, id):
    tutor = Tutor.objects.get(id=id)
    sexo = Sexo.objects.all()
    cat_tipo_sangre = TipoSangre.objects.all()
    return render(request, "edicion_tutor.html", {"tutor": tutor, "sexo": sexo, "cat_tipo_sangre": cat_tipo_sangre})


def EditarTutor(request):
    if request.method == 'POST':
        id = request.POST['id']
        tutor = Tutor.objects.get(id=id)
        formularioTutor = TutorForm(request.POST, request.FILES, instance=tutor)
        if formularioTutor.is_valid():
            formularioTutor.save()
            messages.success(request, 'edit')
            print("Si redireccionó")
            return redirect('listado_tutores')
        else:
            print("Formulario no Válido. No se pudo guardar")
    else:
        return render(request, "listado_tutores.html")


def EliminarTutor(request, id):
    tutor = Tutor.objects.get(id=id)
    tutor.delete()
    messages.success(request, 'delete')
    return redirect('listado_tutores')