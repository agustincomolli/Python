nombre = input("¿Cuál es tu nombre? ")
edad = int(input("¿Qué edad tienes? "))

if nombre == "Agustín":
    print("¡Hola Agustín!")
elif edad < 12:
    print("¡Tú no eres Agustín niño!")
elif edad > 120:
    print("A diferencia de ti, Agustín no es un vampiro inmortal.")
elif edad > 70:
    print("¡Tú no eres Agustín, abuelo!")
else:
    print("¡Tú no eres Agustín!")