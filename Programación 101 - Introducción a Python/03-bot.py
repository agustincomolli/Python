def hacer_calculos():
    print("Vamos a " + comando + " algunos números...")
    ingreso_1 = input("Número 1: ")
    ingreso_2 = input("Número 2: ")
    
    # Convertir variables de texto en variables de números DECIMALES.
    numero_1 = float(ingreso_1)
    numero_2 = float(ingreso_2)
    
    if comando == "sumar":
        operador = "+"
        resultado = numero_1 + numero_2
    elif comando == "restar":
        operador = "-"
        resultado = numero_1 - numero_2
    elif comando == "multiplicar":
        operador = "*"
        resultado = numero_1 * numero_2
    elif comando == "dividir":
        operador = "/"
        resultado = numero_1 / numero_2
    
    # Si el resultado no tiene parte decimal...
    if resultado % 1 == 0.0:
        # Convertirlo en entero.
        resultado = int(resultado)
    else:
        # Redondear el resultado a dos decimales.
        resultado = round(resultado, 2)

    # Convertir el resultado en variable de texto.
    salida = str(resultado)
    print(ingreso_1, operador, ingreso_2 + " = " + salida)

def calcular_lista():
    cant_numeros = input(f"¿Para cuántos números deseas el {comando}? ")
    cant_numeros = int(cant_numeros)
    total = 0

    for contador in range(cant_numeros):
        numero = input(f"Ingrese un número: ")
        total += float(numero)
    
    if comando == "promedio":
        resultado = total / cant_numeros
    else:
        resultado = total
    
    # Si el resultado no tiene parte decimal...
    if resultado % 1 == 0.0:
        # Convertirlo en entero.
        resultado = int(resultado)
    else:
        # Redondear el resultado a dos decimales.
        resultado = round(resultado, 2)

    print(f"\nEl {comando} es: ", resultado)


print("¡Hola soy Bot Icelli, tu bot personal! ^^")
print("Empecemos...")
nombre_usuario = input("¿Cómo te llamas? ")
print("Bienvenido " + nombre_usuario)
terminado = False

while terminado == False:
    comando = input("¿Qué deseas hacer? ")
    if comando == "sumar" or comando == "+":
        hacer_calculos()
    elif comando == "restar" or comando == "-":
        hacer_calculos()
    elif comando == "multiplicar" or comando == "*":
        hacer_calculos()
    elif comando == "dividir" or comando == "/":
        hacer_calculos()
    elif comando == "promedio":
        calcular_lista()
    elif comando == "total":
        calcular_lista()
    elif comando == "pagar":
        print("\n*** Calcular el pago a la romana de una comida ***")
        total_comida = input("Ingrese el total por la comida: $")
        total_comida = float(total_comida)
        personas = input("¿Cuántos son los comensales? ")
        personas = int(personas)
        pagar = total_comida / personas
        print(f"Cada comensal deberá pagar ${pagar}")
    elif comando == "salir":
        print("\n¡Hasta pronto! Que tengas un buen día =)")
        terminado = True
    else:
        print("Lo siento pero no entiendo el comando: \"" + comando + "\"")
 
