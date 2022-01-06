# Coberturas de pizza: escriba un bucle que solicite al usuario que ingrese 
# una serie de coberturas de pizza hasta que ingrese un valor de 'salir'. A 
# medida que ingresan cada ingrediente, imprima un mensaje que diga que 
# agregará ese ingrediente a su pizza.

print("*** Has tu pizza ***")
ingrediente = ""
while ingrediente != "salir":
    ingrediente = input("¿Qué ingrediente desea agregar? ")
    if ingrediente != "salir":
        print(f"Agregando... {ingrediente} a la pizza.")

print("\n¡Marcha una pizza loca!")

# Entradas de cine: una sala de cine cobra diferentes precios de entradas 
# según la edad de la persona. Si una persona es menor de 3 años, la entrada 
# es gratuita; si tienen entre 3 y 12, el boleto es de $ 10; y si son mayores 
# de 12 años, el boleto cuesta $ 15. Escriba un bucle en el que pregunte a los 
# usuarios su edad y luego dígales el costo de la entrada al cine.

edad = 1
while edad != 0:
    edad = int(input("¿Qué edad tienes? [0 = salir] "))
    if 1 <= edad < 3:
        print("Tu entras gratis.")
    elif 3 <= edad <= 12:
        print("Tu entrada cuesta $ 10.")
    elif edad > 12:
        print("Tu entrada cuesta $ 15.")

# Tres salidas: escriba diferentes versiones del ejercicio anterior que realicen 
# cada una de las siguientes acciones al menos una vez:
# • Utilice una prueba condicional en la instrucción while para detener el 
#   ciclo.
# • Utilice una variable activa para controlar la duración del ciclo.
# • Utilice una declaración de interrupción para salir del ciclo cuando el 
#   usuario ingrese un valor de 'salir'.

# Infinito: escribe un bucle que nunca termine y ejecútalo. (Para finalizar el 
# ciclo, presione ctrl-C o cierre la ventana que muestra la salida).
numero = 0
while True:
    numero += 1
    print(f"{numero} - ¡Este bucle nunca acaba!")