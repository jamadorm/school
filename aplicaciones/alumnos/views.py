import psycopg2
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError

from aplicaciones.alumnos.conex.conex import conexion
from aplicaciones.alumnos.forms import AlumnoForm, AlumnoTutorForm
from aplicaciones.alumnos.models import Alumno, AlumnoTutores
from aplicaciones.catalogos.models import Sexo, TipoSangre
from aplicaciones.tutores.models import Tutor


# Create your views here.

def InicioAlumno(request):
    return render(request, "inicio_alumnos.html")


def ListadoAlumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, "listado_alumnos.html", {"alumnos": alumnos})


def NuevoAlumno(request):
    cat_sexo = Sexo.objects.all()
    cat_tipo_sangre = TipoSangre.objects.all()
    if request.method == 'POST':
        formularioAlumno = AlumnoForm(request.POST, request.FILES)
        if formularioAlumno.is_valid():
            formularioAlumno.save()
            messages.success(request, 'new')
            return redirect('listado_alumnos')
        else:
            print("ERROR - No se pudo grabar el formulario")
    else:
        formularioAlumno = AlumnoForm()
    return render(request, "nuevo_alumno.html",
                  {"formularioAlumno": formularioAlumno, "cat_sexo": cat_sexo, "cat_tipo_sangre": cat_tipo_sangre})


def EdicionAlumno(request, id):
    alumno = Alumno.objects.get(id=id)
    sexo = Sexo.objects.all()
    cat_tipo_sangre = TipoSangre.objects.all()
    return render(request, 'editar_alumno.html', {"alumno": alumno, "sexo": sexo, "cat_tipo_sangre": cat_tipo_sangre})


def EditarAlumno(request):
    if request.method == 'POST':
        id = request.POST['id']
        alumno = Alumno.objects.get(id=id)
        formularioAlumno = AlumnoForm(request.POST, request.FILES, instance=alumno)
        if formularioAlumno.is_valid():
            formularioAlumno.save()
            messages.success(request, 'edit')
            return redirect('listado_alumnos')
        else:
            print("ERROR - El formulario no es válido ")
            messages.success(request, 'error')
    else:
        return render(request, "editar_alumno.html")


def EliminarAlumno(request, id):
    alumno = Alumno.objects.get(id=id)
    alumno.delete()
    messages.success(request, 'delete')
    return redirect('listado_alumnos')


def PerfilAlumno(request, id):
    alumno = Alumno.objects.get(id=id)
    tutores = AlumnoTutores.objects.filter(id_alumno=id)
    # print("* * * * * TUTORES * * * * * ")
    # print(tutores.values())
    return render(request, 'perfil_alumno.html', {"alumno": alumno, "tutores": tutores})


def BuscarAlumno(request):
    alumnos = Alumno.objects.all()
    return render(request, 'buscar_alumno.html', {"alumnos": alumnos})


def PerfilAlumnoBuscado(request):
    if request.method == 'POST':
        id = request.POST.get('alumno', 0)
        # print(id)
        # print("si entró")
        # return PerfilAlumno(request,id)
        return redirect('perfil_alumno', id=id)
        # return render(request, 'buscar_alumno.html')
    else:
        print("No entró")
        return render(request, 'buscar_alumno.html')


def TutorAlumno(request):
    alumnos = Alumno.objects.all()
    tutores = Tutor.objects.all()

    if request.method == 'POST':
        alumno = request.POST['id_alumno']
        id_tutor = request.POST['id_tutor']
        tutor_existe = AlumnoTutores.objects.filter(id_alumno=alumno).filter(id_tutor=id_tutor)
        alumno = int(alumno)

        if len(tutor_existe) == 0:  # Si no existe el Tutor, lo asigna.
            formAlumnoTutor = AlumnoTutorForm(request.POST)
            if formAlumnoTutor.is_valid():
                formAlumnoTutor.save()
                message = 'Tutor_agregado'
            return render(request, 'asignar_tutor.html',
                          {"alumnos": alumnos, "tutores": tutores, "formAlumnoTutor": formAlumnoTutor,
                           "message": message, "id_alumno_selected": alumno})
        else:  # Si el tutor existe, manda mensaje de error.
            print('Ya existe tutor para ese alumno')
            message = 'Tutor_existente'
            formAlumnoTutor = AlumnoTutorForm()
            return render(request, 'asignar_tutor.html',
                          {"alumnos": alumnos, "tutores": tutores, "formAlumnoTutor": formAlumnoTutor,
                           "message": message, "id_alumno_selected": alumno})
    else:
        formAlumnoTutor = AlumnoTutorForm()
        return render(request, 'asignar_tutor.html',
                      {"alumnos": alumnos, "tutores": tutores, "formAlumnoTutor": formAlumnoTutor})


# FUNCIÓN PARA UTILIZAR EN AJAX
def DetallesTutor(request):
    if request.method == 'GET':
        id_tutor = request.GET['id']
        id_alumno = request.GET['alumno_id']

        # tutor = list(Tutor.objects.filter(id=id_tutor).values('id', 'nombre'))
        tutor = list(Tutor.objects.filter(id=id_tutor).values())
        parentesco = list(AlumnoTutores.objects.filter(id_alumno=id_alumno).filter(id_tutor=id_tutor).values())
        # print(tutor)
        if (len(tutor) > 0):
            data = {'message': 'Mensaje desde DetallesTutor', 'tutor': tutor, "parentesco": parentesco}
            # print(data)
        else:
            data = {'message': 'Not Found'}
            print(data)

        return JsonResponse(data)  # regresa un listado en formato JSON


def TutoresAsignados(request):
    if request.method == 'GET':
        id_alumno = request.GET['id_alumno']
        tutores = list(AlumnoTutores.objects.filter(id_alumno=id_alumno).values())
        if (len(tutores) > 0):
            data = {'message': 'Si existen tutores asignados', 'tutores': tutores}
            # print(data)
        else:
            data = {'message': 'Not Found'}
            print(data)
    return JsonResponse(data)


def TutorAlumno_multiple(request):
    if request.method == 'POST':
        alumno = request.POST['alumno']
        tutores = request.POST.getlist("tutores[]")
        # print("alumno: ",alumno)
        try:
            cursor = conexion.cursor()
            for tutor in tutores:
                print("Alumno:" + alumno + " - Tutor: " + tutor)
                consulta = "INSERT INTO alumnos_alumnotutores(id_alumno_id, id_tutor_id) VALUES(%s::bigint, %s::bigint)"
                cursor.execute(consulta, (alumno, tutor))
            conexion.commit()

        except psycopg2.Error as e:
            print("Ocurrió un error al insertar: ", e)
        finally:
            conexion.close()

        return redirect('perfil_alumno/' + alumno)
    else:
        alumnos = Alumno.objects.all()
        tutores = Tutor.objects.all()
        return render(request, 'asignar_tutor.html', {"alumnos": alumnos, "tutores": tutores})


def Pruebas(request):
    return render(request, 'borrar.html')
