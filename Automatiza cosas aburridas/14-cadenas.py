mensaje = "Agustín Comolli"
for letra in mensaje[0:7]:
    print(f"*** {letra} ***")

mensaje = "Pocholo un perro travieso."
print(mensaje)
nuevo_mensaje = f"{mensaje[:7]}, el {mensaje[11:]}"
print(nuevo_mensaje)