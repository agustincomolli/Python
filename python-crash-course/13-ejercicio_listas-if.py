usuarios = ["admin", "acomolli", "lmellado", "cgiola", "mfaure", "agomez"]
print("\nLista de usuarios:")

# Recorrer la lista de usuarios e imprimir un saludo.
if usuarios:
    for usuario in usuarios:
        if usuario == "admin":
            print("Hola administrador, ¿le gustaría ver un informe de estado?")
        else:
            print("Hola " + usuario + ", gracias por iniciar sesión nuevamente.")
else:
    print("¡Necesitamos encontrar algunos usuarios!")

usuarios = []
print("\nTodos los usuarios han sido quitados de la lista.")

usuarios_actuales = ["admin", "acomolli", "lmellado", "cgiola", "mfaure", "agomez"]
nuevos_usuarios = ["mromero", "guhart", "acomolli", "mcladera" ,"cgiola"]

for usuario in nuevos_usuarios:
    if usuario in usuarios_actuales:
        print(usuario + ": Este nombre de usuario está en uso.")
    else:
        print(usuario + ": El nombre de usuario está disponible.")

