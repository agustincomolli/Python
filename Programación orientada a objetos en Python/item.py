#!/usr/bin/env python3

class Item():
    def __init__(self, nombre_item) -> None:
        self.nombre = nombre_item
        self.descripcion = None
        self.genero = "m"

    def set_nombre(self, nombre_item):
        self.nombre = nombre_item

    def get_nombre(self):
        return self.nombre

    def set_descripcion(self, descripcion_item):
        self.descripcion = descripcion_item

    def get_descripcion(self):
        return self.descripcion

    def set_genero(self, genero_item):
        self.genero = genero_item

    def get_genero(self):
        return self.genero

    def describir(self):
        if self.genero == "m":
            inicio = "El"
        else:
            inicio = "La"
        
        print(f"{inicio} {self.nombre} está aquí. {self.descripcion}")