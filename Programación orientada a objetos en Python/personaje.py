#!/usr/bin/env python3

class Personaje:
    
    # Crear un personaje.
    def __init__(self, nombre_personaje, descripcion_personaje) -> None:
        self.nombre = nombre_personaje
        self.descripcion = descripcion_personaje
        self.conversacion = None

    # Describir este personaje.
    def describir(self):
        print("¡" + self.nombre + " está aquí!")
        print(self.descripcion)

    # Establecer lo que dirá este personaje cuando se le hable.
    def set_conversacion(self, conversacion):
        self.conversacion = conversacion

    # Hablar con este personaje.
    def hablar(self):
        if self.conversacion is not None:
            print(f"[{self.nombre} dice]: {self.conversacion}")
        else:
            print(f"{self.nombre} no quiere hablar contigo")
    
    # Pelear con este personaje.
    def pelear(self, item_de_combate):
        print(f"{self.nombre} no quiere pelear contigo.")
        return True

class Enemigo(Personaje):
    enemigos_a_derrotar = 0
    
    # Crear enemigo.
    def __init__(self, nombre_personaje, descripcion_personaje) -> None:
        super().__init__(nombre_personaje, descripcion_personaje)
        self.debilidad = None
        self.enemigos_a_derrotar += 1

    def set_debilidad(self, debilidad_enemigo):
        self.debilidad = debilidad_enemigo

    def get_debilidad(self):
        return self.debilidad

    def pelear(self, item_de_combate):
        if item_de_combate == self.debilidad:
            print(f"Te defiendes de {self.nombre} con {item_de_combate}")
            self.enemigos_a_derrotar -= 1
            return True
        else:
            print(f"¡{self.nombre} te aplasta, aventurero insignificante!")
            return False
    
    def robar(self):
        print(f"Robas de {self.nombre}")
        # ¿Cómo vas a decidir qué tiene que robar este personaje?


class Amigo(Personaje):
    def __init__(self, nombre_personaje, descripcion_personaje) -> None:
        super().__init__(nombre_personaje, descripcion_personaje)
        self.sentimiento = None

    def abrazar(self):
        print(f"¡{self.nombre} te abraza de vuelta!")
    # ¿Qué otros métodos podría tener tu clase Friend?