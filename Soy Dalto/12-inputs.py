# Pedir al usuario que introduzca un dato.
name = input("¿Cómo te llamas?: ")
print(f"Bienvenido {name}")

# La función input siempre devuelve un string.
age = int(input("\n¿Cuántos año tienes?: "))
if age >= 18:
    print("¡Bien, ya eres mayor de edad!")
else:
    print("Todavía eres chico")