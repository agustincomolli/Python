print("\nDesafío: \n*********")
respuesta = input("¿Desea continuarla tarea? [s|n]: ")

if respuesta == "no" or respuesta == "n":
    print("Saliendo.")
elif respuesta == "si" or respuesta == "s":
    print("Continuando...")
    print("¡Tarea completada!")
else:
    print("Vuelva a intentarlo y responda con sí o no.")