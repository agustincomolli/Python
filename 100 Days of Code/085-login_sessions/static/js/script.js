// Obtener el botón cancelar
const btn_cancel = document.getElementById("btn-cancel")

function go_index() {
    // Redirigir a la página principal.
    window.location.href = "/"
}


// Agregar el evento click
btn_cancel.addEventListener("click", go_index)