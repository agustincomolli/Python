#!/usr/bin/env python3

from random import randint

jugador_piedra = '''
    _______
---'   ____)
      (_____)
      (_____)         PIEDRA
      (____)
---.__(___)
'''

jugador_papel = '''
    _______
---'   ____)____
          ______)
          _______)    PAPEL
         _______)
---.__________)
'''

jugador_tijera = '''
    _______
---'   ____)____
          ______)
       __________)    TIJERA
      (____)
---.__(___)
'''

computadora_piedra = '''
  _______
 (____   '---
(_____)
(_____)               PIEDRA
 (____)
  (___)__.---
'''

computadora_papel = '''
       _______
  ____(____   '---
 (______
(_______              PAPEL
 (_______
   (__________.---    
'''

computadora_tijera = '''
       _______
  ____(____   '---
 (______
(__________           TIJERA
      (____)
       (___)__.---
    '''

vs = '''
____   ____     
\   \ /   /_____
 \   Y   /  ___/
  \     /\___ \ 
   \___//____  >
             \/ 
'''

jugador = input("¿Piedra (r), papel (p) o tijera (t)? ")
if jugador == "r":
    mano_jugador = jugador_piedra
elif jugador == "p":
    mano_jugador = jugador_papel
elif jugador == "t":
    mano_jugador = jugador_tijera
else:
    print("¡ERROR! ¡No ingresó una opción correcta!")
    exit()

elegido = randint(1, 3)
if elegido == 1:
    mano_computadora = computadora_piedra
    computadora = "r"
elif elegido == 2:
    mano_computadora = computadora_papel
    computadora = "p"
else:
    mano_computadora = computadora_tijera
    computadora = "t"

print(mano_jugador, vs, mano_computadora)

if jugador == computadora:
    print("*** EMPATE ***")
elif jugador == "r" and computadora == "p":
    print("*** PERDISTE! :'( ***")
elif jugador == "r" and computadora == "t":
        print("*** ¡GANASTE! =) ***")
elif jugador == "p" and computadora == "r":
    print("*** ¡GANASTE! =) ***")
elif jugador == "p" and computadora == "t":
    print("*** PERDISTE! :'( ***")
elif jugador == "t" and computadora == "r":
    print("*** PERDISTE! :'( ***")
elif jugador == "t" and computadora == "p":
    print("*** ¡GANASTE! =) ***")
