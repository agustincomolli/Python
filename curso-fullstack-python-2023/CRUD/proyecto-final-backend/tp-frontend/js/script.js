let formulario = document.getElementById("formulario");

formulario.addEventListener("submit", function (e) {
    e.preventDefault(); //Evita que se recargue la página

    let form = e.target;



    let datos = new FormData(form);

    datos.append("nombre", "Nombre del producto");
    datos.append("precio", "99.99");
    datos.append("stock", "10");
    datos.append("imagen", "imageFile");

    let endpoint = "http://127.0.0.1:5000/producto";

    console.log(form);
    fetch(endpoint, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
          },
        body: datos,
    }).then(function (response) {
        if (response.ok) {
            alert("Producto registrado con éxito");
        } else {
            console.log(response);
            alert("Error al registrar el producto");
        }
    }).catch(function (error) {
        console.log(error);
    });

});
