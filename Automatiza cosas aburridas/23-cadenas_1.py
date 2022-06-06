while True:
    edad = input("Ingrese su edad: ")
    if edad.isdecimal():
        break
    print("ERROR. Ingrese un número para su edad.\n")

while True:
    print("Elija una contraseña (letras y números solamente).")
    contraseña = input("Contraseña: ")
    if contraseña.isalnum():
        break
    print("Las  contraseñas solo pueden tener letras y números.\n")