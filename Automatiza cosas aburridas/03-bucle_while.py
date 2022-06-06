nombre = ""

while nombre != "salir":
    nombre = input("Escriba su nombre: ")

    if nombre != "Agustín":
        continue
    
    contraseña = input("¡Hola Agustín! ¿Cuál es la contraseña? (es un pez): ")

    if contraseña == "pez espada":
        print("Acceso otorgado")
        break

print("¡Gracias!")

