#!/usr/bin/env python3

class Habitacion():

    numero_habitaciones = 0

    # Método constructor.
    def __init__(self, nombre_habitacion) -> None:
        # Definir propiedades.
        self.nombre = nombre_habitacion
        self.genero = "m"
        self.descripcion = None
        self.habitaciones_vinculadas = {}
        self.personaje = None
        self.item = None

        # Aumentar el número de habitaciones.
        Habitacion.numero_habitaciones += 1

    # Definir propiedades.
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre_habitacion):
        self._nombre = nombre_habitacion

    # Definir setters y getters para establecer o recuperar valores
    # de las propiedades.
    
    # def set_nombre(self, nombre_habitacion):
    #     self.nombre = nombre_habitacion
    
    # def get_nombre(self):
    #     return self.nombre

    def set_genero(self, genero_habitacion):
        '''m o f'''
        self.genero = genero_habitacion

    def get_genero(self):
        return self.genero

    def set_descripcion(self,descripcion_habitacion):
        self.descripcion = descripcion_habitacion

    def get_descripcion(self):
        """ 
        Devuelve una cadena con la descripción de la habitación.
        """
        return self.descripcion

    def set_personaje(self, nuevo_personaje):
        self.personaje = nuevo_personaje
    
    def get_personaje(self):
        return self.personaje

    def set_item(self, nombre_item):
        self.item = nombre_item
    
    def get_item(self):
        return self.item

    def describir(self):
        print(self.descripcion)

    # Agregar valores al diccionario habitaciones_vinculadas.
    def vincular_habitacion(self, habitacion_a_vincular, direccion):
        self.habitaciones_vinculadas[direccion] = habitacion_a_vincular

    def get_detalles(self):
        # Mostrar detalles de la habitación actual...
        print(self.nombre.title())
        print("-" * 15)
        print(self.descripcion)
        
        # Mostrar las habiaciones vinculadas.
        for direccion in self.habitaciones_vinculadas:
            habitacion = self.habitaciones_vinculadas[direccion]
            if habitacion.genero == "m":
                inicio = "El"
            else:
                inicio = "La"
            print(f"{inicio} {habitacion.nombre} está al {direccion}.")

    def mover(self, direccion):
        if direccion in self.habitaciones_vinculadas:
            return self.habitaciones_vinculadas[direccion]
        else:
            print("¡No puedes ir en esa dirección!")
            return self