# Extraer nombres
# 
# Utilice una lista de comprensión para crear una nueva lista que 
# first_names contenga solo los primeros nombres namesen minúsculas.

names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names = [name[:name.find(" ")].lower() for name in names] # write your list comprehension here

print("Primeros nombres en minúsculas: ", first_names)

# Múltiplos de tres

# Utilice una lista de comprensión para crear una lista multiples_3 que 
# contenga los primeros 20 múltiplos de 3.

multiples_3 = [i * 3 for i in range(1, 21)] # write your list comprehension here
print("Primeros 20 múltiplos de 3: ", multiples_3)

# Filtrar nombres por puntajes

# Use una lista de comprensión para crear una lista de nombres passed
# que solo incluya aquellos que obtuvieron una puntuación de al menos 65.

scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }

passed = [name for name, score in scores.items() if score >= 65] # write your list comprehension here

print(passed)