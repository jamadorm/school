function convertir_fecha_nac(input_fecha_nac){

    fecha_nac = input_fecha_nac;
    fecha_nac = fecha_nac.split(" ");
    dia=fecha_nac[0].padStart(2, 0);
    mes_aux = fecha_nac[2];

    switch (mes_aux) {
          case 'Enero':
            mes = "01";
            break;
          case 'Febrero':
            mes = "02";
            break;
          case 'Marzo':
            mes = "03";
            break;
          case 'Abril':
            mes = "04";
            break;
          case 'Mayo':
            mes = "05";
            break;
          case 'Junio':
            mes = "06";
            break;
          case 'Julio':
            mes = "07";
            break;
          case 'Agosto':
            mes = "08";
            break;
          case 'Septiembre':
            mes = "09";
            break;
          case 'Octubre':
            mes = "10";
            break;
          case 'Noviembre':
            mes = "11";
            break;
          case 'Diciembre':
            mes = "12";
            break;
        }
    año = fecha_nac[4];

    fecha_nacimiento = año+"-"+mes+"-"+dia;
    fecha_nacimiento = fecha_nacimiento.toString();
    return fecha_nacimiento;
}


function validar_re_pass(pass1,pass2)
    {
        var p1 = pass1,
            p2 = pass2;

            if (p2.value !== "")
            {
                   if (p1.value === p2.value) {
                        p1.className = "form-control is-valid";
                        p2.className = "form-control is-valid";
                        return true;
                    } else {
                        //alert('Las contraseñas no coinciden, favor de revisar.');
                        p1.className = "form-control is-invalid";
                        p2.className = "form-control is-invalid";
                        return true;
                    }
            }
    }



//Funciones para manipulación de registros en tablas

function deleteRow(element){
        var i = element.parentNode.parentNode.parentNode.rowIndex;
        var select = document.getElementById('id_alumno_select');

        id_alumno = document.getElementById("tabla_alumnos").rows[i].cells[0].innerText;
        nombre_alumno = document.getElementById("tabla_alumnos").rows[i].cells[1].innerText;
        //alert(nombre_alumno);

        const option = document.createElement('option');
        option.value = id_alumno;
        option.text = nombre_alumno;
        select.appendChild(option); //insertamos el elemento
	    select.value = id_alumno;  //insertamos el valor

        document.getElementById("tabla_alumnos").deleteRow(i);
    }

    function valorSelect(){
        var select = document.getElementById('id_alumno_select');
        //alert(select.value);
        var selected = select.options[select.selectedIndex].text;
        alert(selected);

    }

    function AgregarAlumno(){
        var select = document.getElementById('id_alumno_select');
        var id_alumno = select.value;
        var datos_alumno = select.options[select.selectedIndex].text;
        select.options[select.selectedIndex].remove();

        document.getElementById('tabla_alumnos').insertRow(-1).innerHTML = '<td>' + id_alumno + '</td>' +

                              '<td>' + datos_alumno + '</td>' +
                              '<td>' +
                                  '<div class="align-items-center">' +
                                        '<input type="hidden" id="id_id_alumno" name="id_alumno[]" value="' + id_alumno + '">' +
                                      '<a href="/alumnos/perfil_alumno/' + id_alumno + '" target="_blank" type="button" class="btn mb-1 btn-light-primary btn-circle btn-sm d-inline-flex align-items-center justify-content-center" data-bs-toggle="tooltip" data-bs-placement="top" data-bs-original-title="Ver Detalles">' +
                                        '<i class="fs-5 ti ti-id text-primary"></i>' +
                                      '</a>' +
                                      '<a onclick="deleteRow(this)" class="btn mb-1 btn-light-danger delete btn-circle btn-sm d-inline-flex align-items-center justify-content-center" data-bs-toggle="tooltip" data-bs-placement="top" data-bs-original-title="Quitar del listado">' +
                                        '<i class="fs-5 ti ti-trash-x-filled text-primary"></i>' +
                                      '</a>' +
                                  '</div>' +
                              '</td>';


    }