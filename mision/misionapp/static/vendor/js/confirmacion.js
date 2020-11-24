function confirmarEliminacion(id) {
    Swal.fire({
        title: 'Estas seguro?',
        text: "No podras disolver esta accion!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si, Eliminar!',
        cancelButtonText: 'Cancelar'
      }).then((result) => {
        if (result.isConfirmed) {
         window.location.href = "/elimina_articulo/"+id+"/";
        }
      })
}


function confirmarEliminacionPersonal(id) {
  Swal.fire({
      title: 'Estas seguro?',
      text: "No podras disolver esta accion!",
      icon: 'warning',
      showCancelButton: true,
      confirmButtonColor: '#3085d6',
      cancelButtonColor: '#d33',
      confirmButtonText: 'Si, Eliminar!',
      cancelButtonText: 'Cancelar'
    }).then((result) => {
      if (result.isConfirmed) {
       window.location.href = "/elimina_personal/"+id+"/";
      }
    })
}