import sys

# Configure una lista para que funcione nuestro código que omita el primer argumento CLI, 
# que es el nombre de nuestro script (list_iteration.py)
order_of_succession = sys.argv
order_of_succession.pop(0)

for index, item in enumerate(order_of_succession,start=1):
    print(f"{index}. {item}")