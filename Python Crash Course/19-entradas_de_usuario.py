prompt = "Si nos dice quién es, podemos personalizar los mensajes que ve."
prompt += "\n¿Cuál es su primer nombre? "

nombre = input(prompt)

print(f"\n¡Hola {nombre}!")

altura = int(input("¿Cuál es tu altura? "))
if altura >= 90:
    print("\n¡Eres lo suficientemente alto para subir a una montaña rusa!")
else:
    print("\nTe falta altura para subir a la montaña rusa." + 
        "\nPodrás subir cuando seas un poco mayor.")

numero = int(input("\nIngresa un número y te diré si es par o impar: "))

if numero % 2 == 0:
    print(f"\nEl número {numero} es par.")
else:
    print(f"\nEl número {numero} es impar.")