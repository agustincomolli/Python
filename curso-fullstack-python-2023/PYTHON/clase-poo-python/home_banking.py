#CLASES:

#-----------------------#
#Clase Banco
class Banco:
    def __init__(self):
        self.cliente1 = Cliente("German")
        self.cliente2 = Cliente("Luis")
        self.cliente3 = Cliente("Ana")

    def operar(self):
        self.cliente1.despositar(100)
        self.cliente2.despositar(150)
        self.cliente3.despositar(200)
        self.cliente3.extraer(150)

#-----------------------#
#Clase Cliente

class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.saldo = 0


    def despositar(self, monto):
        self.saldo += monto # self.saldo = self.saldo + monto

    def extraer(self, monto):
        self.saldo -= monto

    def retornar_saldo(self):
        return self.saldo
    
    def imprimir(self):
        print("Nombre:", self.nombre, "Saldo:", self.saldo)


#Programa principal


banco1 = Banco() #Instanciamos la clase Banco y creamos el objeto banco1
banco1.operar() #Llamamos al metodo operar del objeto banco1

banco2 = Banco() #Instanciamos la clase Banco y creamos el objeto banco2

banco2.operar() #Llamamos al metodo operar del objeto banco2

banco2.cliente1.imprimir() #Llamamos al metodo imprimir del objeto cliente1 del objeto banco2
banco2.cliente2.imprimir() #Llamamos al metodo imprimir del objeto cliente2 del objeto banco2
banco2.cliente3.imprimir() #Llamamos al metodo imprimir del objeto cliente3 del objeto banco2

banco1.cliente1.imprimir() #Llamamos al metodo imprimir del objeto cliente1 del objeto banco1
banco1.cliente2.imprimir() #Llamamos al metodo imprimir del objeto cliente2 del objeto banco1
banco1.cliente3.imprimir() #Llamamos al metodo imprimir del objeto cliente3 del objeto banco1
    