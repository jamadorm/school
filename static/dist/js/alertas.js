$('#btn_guardar').click(function(){
    Swal.fire({
      icon: 'success',
      title: '<i class="ti ti-device-floppy"></i>' + 'Registro Guardado',
      html: 'El registro se guardó correctamente.',
      timer: 3000,
      timerProgressBar: true,
      willClose: () => {
        clearInterval(timerInterval)
      }
    })
});
$('#btn_actualizar').click(function(){
    Swal.fire({
        position: 'top-end',
        icon: 'success',
        title: 'Se actualizo el registro de la manera correcta',
        showConfirmButton: false,
        timer: 1500
      })
});
$('#btn_eliminar').click(function(ev){
    ev.preventDefault();
    Swal.fire({
        title: '¿Esta seguro de eliminar el registro?',
        text: "Verifique antes de continuar",
        icon: 'warning',
        showDenyButton: false,
        showCancelButton: true,
        confirmButtonText: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si, eliminar!'
      }).then((result) => {
              if (result.isConfirmed) {
                Swal.fire('Saved!', '', 'success')
                window.location.href = "inicio";
              } else if (result.isDenied) {
                Swal.fire('Changes are not saved', '', 'info')
              }
             }
       )
});



function prueba(e){
    alert(e.getAttribute("data-message"));
}


function registrado(){
    Swal.fire({
      icon: 'success',
      title: '<i class="ti ti-device-floppy"></i>' + 'Registro Guardado',
      html: 'El registro se guardó correctamente.',
      timer: 3000,
      timerProgressBar: true,
      willClose: () => {
        clearInterval(timerInterval)
      }
    })
}


function eliminar(e){
    href = e.getAttribute("data-message")
    Swal.fire({
        title: '¿Esta seguro de eliminar el registro?',
        text: "Verifique antes de continuar",
        icon: 'warning',
        showDenyButton: false,
        showCancelButton: true,
        confirmButtonText: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: '<i class="ti ti-thumb-up"></i>'+' Confirmar',
        cancelButtonText: 'Cancelar'
      }).then((result) => {
              if (result.isConfirmed) {
                //Swal.fire('Saved!', 'Desde mi función', 'success')
                window.location.href = href;
              }
             }
       )
}