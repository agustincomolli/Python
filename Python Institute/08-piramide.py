""" 
Un niño y su padre, un programador de computadoras, juegan con bloques de 
madera. Están construyendo una pirámide.

Su pirámide es un poco rara, ya que en realidad es una pared en forma de 
pirámide, es plana. La pirámide se apila de acuerdo con un principio simple: 
cada capa inferior contiene un bloque más que la capa superior.

Tu tarea es escribir un programa que lea la cantidad de bloques que tienen los 
constructores, y generar la altura de la pirámide que se puede construir 
utilizando estos bloques.

Nota: La altura se mide por el número de capas completas: si los constructores 
no tienen la cantidad suficiente de bloques y no pueden completar la siguiente 
capa, terminan su trabajo inmediatamente.

"""

blocks = int(input("Ingresa el número de bloques: "))

#
# Escribe tu código aquí.
#

height = 0
while height < blocks:
    height += 1
    blocks -= height

print("La altura de la pirámide:", height)