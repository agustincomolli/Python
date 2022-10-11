"""
Cree un programa de inventario.py con una lista:

airplane_toys = [ 898, 732, 543, 878 ]
Cada elemento de la lista es la cantidad de una pieza para el avión de juguete.

Suponga que el número óptimo de partes es [ 1000, 1000, 1000, 1000 ]. ¿Puedes 
averiguar lo siguiente usando las funciones de lista integradas?

¿Qué parte del avión de juguete extrañamos más? Use min()para encontrar los 
valores mínimos en cada lista.
¿Hay una pieza de juguete de avión que estamos sobrecargando? Use max()para 
encontrar el valor máximo en cada lista.

"""

print("Aviones de juguete 🛩️")

airplane_toys = [ 898, 732, 543, 878 ]

print(f"El valor mínimo es {min(airplane_toys)}")
print(f"El valor máximo es {max(airplane_toys)}")