fetch('https://germancodoacodo.pythonanywhere.com/productos')
.then(response => response.json())
.then(data => {
    

data.forEach(element => {

    const row = document.createElement('tr');
    
    const id = document.createElement('td');
    id.textContent = element.id;
    row.appendChild(id);

    const nombre = document.createElement('td');
    nombre.textContent = element.nombre;
    row.appendChild(nombre);

    const precio = document.createElement('td');
    precio.textContent = element.precio;
    row.appendChild(precio);

    const stock = document.createElement('td');
    stock.textContent = element.stock;
    row.appendChild(stock);

    const imagen = document.createElement('td');
    imagen.textContent = element.imagen;
    row.appendChild(imagen);

    document.getElementById('productTable').appendChild(row);

    
});

});