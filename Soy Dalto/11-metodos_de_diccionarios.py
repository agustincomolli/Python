user_data = {
    "nombre": "Agustín",
    "apellido": "Comolli",
    "edad": 46,
    "email": "agustincomolli@gmail.com"
}

# Obtener los nombres de las claves de un diccionario.
print(f"Claves del diccionario:\n{user_data.keys()}")

# Obtener un valor del diccionario a través de su clave.
print(f"\nNombre: {user_data.get('nombre')}")

# Eliminar un elemento del diccionario.
user_data.pop("edad")
print(f"\nSe borró la clave 'edad':\n{user_data}")

# Eliminar todos los elementos de un diccionario.
user_data.clear()
print(f"Se bor\n{user_data}")