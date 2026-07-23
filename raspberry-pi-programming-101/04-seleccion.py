frase = input("Háblame: ")

if frase == "Hola" or frase == "hola":
    print("¡Hola! ¿Cómo estás?")
elif frase == "¿Cómo te llamas?" or frase == "¿Cuál es tu nombre?":
    print("Mi nombre es Bot... Bot Icelli.")
elif frase == "¿Cómo estás?":
    print("Todo bien, gracias.")
else:
    print("Lo siento, no entiendo esto: \"" + frase + "\"")

frase = input("Y tú, cómo te llamas? ")

print("Hola " + frase + " bienvenido al programa.")

edad = int(input("¿Cuántos años tienes? "))

if edad < 11:
    print("¡Eres un niño!")
elif edad > 11 and edad < 18:
    print("¡Patiño, Patiño... esas bolas no son de niño!")
elif edad > 18 and edad < 40:
    print("¡Ah, sos joven!")
elif edad > 40 and edad < 55:
    print("¡Sos un pendeviejo!")
elif edad > 55 and edad < 65:
    print("Loco, ya no te cocinas al primer hervor.")
else:
    print("Sos un viejo choto.")

print("¡Adiós!")