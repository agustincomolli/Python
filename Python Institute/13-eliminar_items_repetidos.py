"""
Tu tarea es escribir un programa que elimine todas las repeticiones de números 
de la lista. El objetivo es tener una lista en la que todos los números 
aparezcan no más de una vez.
"""

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
print("Lista original:")
print(my_list)

temp_list =[]
for item in my_list:
    if item not in temp_list:
        temp_list.append(item)

my_list = temp_list
print("La lista con elementos únicos:")
print(my_list)