# Ejemplo de implementación de una pila con el enfoque de programación
# orientada a objetos.-
class Pila():
    def __init__(self):
        self.__ListaPila = []
    
    def push(self, valor):
        self.__ListaPila.append(valor)

    def pop(self):
        valor = self.__ListaPila[-1]
        del self.__ListaPila[-1]
        return valor

class SumarPila(Pila):
    def __init__(self):
        Pila.__init__(self)
        self.__suma = 0
    
    def push(self, valor):
        self.__suma += valor
        Pila.push(self, valor)

    def pop(self):
        valor = Pila.pop(self)
        self.__suma -= valor
        return valor

    def getSuma(self):
        return self.__suma

objPila = SumarPila()

for i in range(5):
    objPila.push(i)

print(objPila.getSuma())

for i in range(5):
    print(objPila.pop())
