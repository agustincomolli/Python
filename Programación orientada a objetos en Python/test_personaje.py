#!/usr/bin/env python3

from personaje import Enemigo

dave = Enemigo("Dave", "Un zombi maloliente")

dave.describir()
dave.set_debilidad("luz")
dave.set_conversacion("¿Qué pasa viejo?")
dave.hablar()

print("¿Con qué lucharás?")
lucha_con = input()

dave.pelear(lucha_con)