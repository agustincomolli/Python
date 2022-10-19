"""
"99 Bottles of Beer" es una vieja canción que los niños molestos cantaban 
en los viajes por carretera para pasar el tiempo.

Cree un programa 99_bottles.py y use un forbucle y una función range() para 
imprimir todos los versos de "99 Bottles of Beer".

99 botellas de cerveza en la pared

99 botellas de cerveza

Toma una, pásala

98 botellas de cerveza en la pared
"""

for i in range(99, 0, -1):
    print(f"{i} botellas de cerveza en la pared")
    print(f"{i} botellas de cerveza")
    print("Toma una, pásala")
