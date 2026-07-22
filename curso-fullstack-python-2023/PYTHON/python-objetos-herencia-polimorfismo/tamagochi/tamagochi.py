class Tamagochi:
    def __init__(self, nombre, hambre, energia, animo):
        self.nombre = nombre
        self.hambre = hambre
        self.energia = energia
        self.animo = animo

    def jugar(self):
        self.hambre += 10 # self.hambre = self.hambre + 10
        self.energia -= 10 # self.energia = self.energia - 10
        self.animo += 10 # self.animo = self.animo + 10

    def alimentar(self):
        self.hambre -= 10 # self.hambre = self.hambre - 10
        self.energia += 10 # self.energia = self.energia + 10
        self.animo += 10 # self.animo = self.animo + 10

    def dormir(self):
        self.hambre += 10 # self.hambre = self.hambre + 10
        self.energia += 10 # self.energia = self.energia + 10
        self.animo += 10 # self.animo = self.animo + 10

    def __str__(self): #metodo para imprimir los atributos del objeto
        return 'Nombre:{}, Hambre: {}, Energia: {}, Animo: {}'.format(self.nombre, self.hambre, self.energia, self.animo)

#PROGRAMA PRINCIPAL

tamagochi1 = Tamagochi("Pepito", 50, 50, 50) #creamos un objeto de la clase Tamagochi

tamagochi1.jugar() #llamamos al metodo jugar
tamagochi1.alimentar() #llamamos al metodo alimentar
tamagochi1.dormir() #llamamos al metodo dormir
tamagochi1.jugar() #llamamos al metodo jugar
tamagochi1.jugar() #llamamos al metodo alimentar
tamagochi1.jugar() #llamamos al metodo alimentar


print("Nombre: ", tamagochi1.nombre)

print(tamagochi1)