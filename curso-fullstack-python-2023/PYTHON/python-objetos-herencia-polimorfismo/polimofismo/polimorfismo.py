#Polimorfismo: Es la habilidad de tomar varias formas, en este caso, un mismo método puede comportarse de diferentes maneras.


class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        raise NotImplementedError("Subclase debe implementar el metodo abstracto")

class Gato(Animal):
    def hablar(self):
        return self.nombre + " dice miau"
    
class Perro(Animal):
    def hablar(self):
        return self.nombre + " dice guau"
    
class Patito(Animal):
    def hablar(self):
        return self.nombre + " dice cuak"
    

#Programa principal

#creamos los objetos

gato = Gato("Bigotes")

perro = Perro("Firulais")

patito = Patito("Lucas")


print(gato.hablar())
print(perro.hablar())
print(patito.hablar())




