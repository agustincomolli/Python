 # Usar la función isnumeric(). La función isnumeric() devuelve un 
 # valor booleano si el valor de cadena se puede convertir en un valor numérico.
print("\nPaso 1: \n********")

valor_numerico = "7"
print("¿\"7\" es un número?", valor_numerico.isnumeric())

valor_cadena = "Agustín"
print("¿\"Agustín\" es un número?",valor_cadena.isnumeric())

# Validar los datos de entrada.
print("\nPaso 2: \n********")

primer_valor = input("Ingrese el primer número: ")
if primer_valor.isnumeric() == False:
    print("El valor ingresado NO es un número.")
    exit() # Finalizar la ejecución del programa.

segundo_valor = input("Ingrese el segundo número: ")
if segundo_valor.isnumeric() == False:
    print("El valor ingresado NO es un número.")
    exit()

primer_valor = int(primer_valor)
segundo_valor = int(segundo_valor)

suma = primer_valor + segundo_valor

print(f"La suma es: {suma}")

# Usar el operador lógico or.
print("\nPaso 3: \n********")

primer_valor = input("Ingrese el primer valor: ")
segundo_valor = input("Ingrese el segundo valor: ")
if primer_valor.isnumeric() == False or segundo_valor.isnumeric() == False:
    print("¡Por favor ingrese solamente números!")
    exit()

primer_valor = int(primer_valor)
segundo_valor = int(segundo_valor)

suma = primer_valor + segundo_valor

print(f"La suma es {suma}")