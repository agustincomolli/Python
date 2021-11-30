# Definir la clase Pila
class Pila:
    def __init__(self):
        # Crear la variable oculta que tendrá la lista de la pila.
        self.__listaPila = []

    # Agregar un valor al final de la pila.
    def push(self, nuevoValor):
        self.__listaPila.append(nuevoValor)
        print("{} se agregó a la pila.".format(nuevoValor))
    
    # Eliminar el último valor de la pila.
    def pop(self):
        valor = self.__listaPila[-1]
        del self.__listaPila[-1]
        print("{} se eliminó de la pila".format(valor))
        return valor

primeraPila = Pila()

primeraPila.push("Agustín")
primeraPila.push("Lorena")
primeraPila.push("Carlitos")

primeraPila.pop()