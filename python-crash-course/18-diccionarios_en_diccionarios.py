usuarios = {
    "acomolli" : {
        "nombre" : "agustín",
        "apellido" : "comolli",
        "ubicación" : "cañuelas"
        },
    "lmellado" : {
        "nombre" : "lorena",
        "apellido" : "mellado",
        "ubicación" : "san andrés"
        }
    }

for nombre_usuario, info_usuario in usuarios.items():
    print("\nUsuario: " + nombre_usuario)
    nombre_completo = info_usuario["nombre"] + " " + info_usuario["apellido"]
    ubicacion = info_usuario["ubicación"]

    print("\tNombre: " + nombre_completo.title())
    print("\tUbicación: " + ubicacion.title())