print("*** Identificador de Generaciones ***\n")

year = int(input("¿En qué año naciste? "))

if year >= 1883 and year <= 1900:
    generation = "perdida 🔍"
elif year > 1900 and year <= 1927:
    generation = "grandiosa 🤪"
elif year > 1927 and year <= 1945:
    generation = "silenciosa 🤫"
elif year > 1945 and year <= 1964:
    generation = "baby boomer 👶"
elif year > 1964 and year <= 1980:
    generation = "x 🧑🏻‍🎤"
elif year > 1980 and year <= 1996:
    generation = "millennial 📱"
elif year > 1996 and year <= 2012:
    generation = "z 💤"
elif year > 2012:
    generation = "Alfa 🧟"
else:
    print("¡Prueba otra vez! 😭")
    exit

print("\nLas personas de", year, "pertenecen a la generación", generation.capitalize())