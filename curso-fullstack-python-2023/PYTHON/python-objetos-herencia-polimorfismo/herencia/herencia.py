#La herencia en pyhton es una forma de reutilizar codigo, es decir, una clase puede heredar de otra clase sus atributos y metodos.

#CLASE PADRE o SUPERCLASE o CLASE BASE
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return 'Nombre: {}, Precio: {}'.format(self.nombre, self.precio)

#CLASES HIJAS
class Libro(Producto): #la clase Libro hereda de la clase Producto
    def __init__(self, codigo, isbn):
        self.codigo = codigo
        self.isbn = isbn

class Adorno(Producto): #la clase Adorno hereda de la clase Producto
    def __init__(self, estilo):
        self.estilo = estilo  

class Alimento(Producto):
    def __init__(self, productor, distribuidor):
        self.productor = productor
        self.distribuidor = distribuidor

class Herramienta(Producto):
    def __init__(self, material):
        self.material = material

# Programa principal

unLibro = Libro(10, "20") #creamos un objeto de la clase Libro

unLibro.nombre = "El principito" #modificamos el atributo nombre de la clase Libro
unLibro.precio = 150 #modificamos el atributo precio de la clase Libro

print(unLibro) #imprimimos el objeto unLibro

unAdorno = Adorno("Moderno") #creamos un objeto de la clase Adorno

unAdorno.nombre = "Vaso" #modificamos el atributo nombre de la clase Adorno
unAdorno.precio = 100 #modificamos el atributo precio de la clase Adorno

print(unAdorno) #imprimimos el objeto unAdorno

unAlimento = Alimento("La Campagnola", "La Serenisima") #creamos un objeto de la clase Alimento

unAlimento.nombre = "Tomate" #modificamos el atributo nombre de la clase Alimento

unAlimento.precio = 50 #modificamos el atributo precio de la clase Alimento

print(unAlimento) #imprimimos el objeto unAlimento
