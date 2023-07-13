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