#Python (POO)

# Una Clase es un Modelo/Plantilla que se utiliza para crear objetos que comparten un mismo comportamiento(metodos), estado() e identidad (Indentificador del objeto).
# Una Clase contiente Atributos y Metodos

# Atributos: Son las caracteristicas que pueden tener un objeto.

# Ejemplo: color, forma, tamaño, etc.

# Metodos: Son las acciones que puede realizar un objeto.

# Ejemplo: caminar, correr, saltar, etc.


class Persona:  # Definimos la clase Persona
    def __init__(self, nombre, piernas, brazos, dni, edad):  # Metodo constructor de la clase Persona
        self.nombre = nombre  # Atributo nombre
        self.piernas = piernas  # Atributo piernas
        self.brazos = brazos  # Atributo brazos
        self.dni = dni  # Atributo dni
        self.edad = edad  # Atributo edad

    def __str__(self):  # Metodo que se ejecuta cuando se imprime el objeto
        return 'Nombre: ' + self.nombre + ' DNI: ' + self.dni + ' Edad: ' + str(self.edad) + ' años'

   # def __del__(self):  # Metodo destructor de la clase Persona
   #     print("Se ha eliminado el objeto", self.nombre)

    def saludar(self):  # Metodo de la clase Persona
        print("Hola, soy", self.nombre, "y tengo", self.edad, "años")  # self: Hace referencia al objeto que se esta ejecutando
              
    def despedir(self):  # Metodo de la clase Persona
        print("Adios, me voy")

    def caminar(self):  # Metodo de la clase Persona self: Hace referencia al objeto que se esta ejecutando
        print("Estoy caminando")


# PROGRAMA PRINCIPAL


# Instanciar una clase: Crear un objeto a partir de una clase.
# Instanciamos la clase Persona y creamos el objeto persona1
persona1 = Persona("pirulo", 2, 2, "33999999", 30)

# Instanciamos la clase Persona y creamos el objeto persona2
persona2 = Persona("jose", 2, 2, "203333333", 50)

print(persona1.dni)  # Imprimimos el atributo brazos del objeto persona1
print(persona1.edad)  # Imprimimos el atributo brazos del objeto persona1


print(persona2.dni)  # Imprimimos el atributo brazos del objeto persona2
print(persona2.edad)  # Imprimimos el atributo brazos del objeto persona2

persona1.saludar()  # Llamamos al metodo saludar del objeto persona1

persona2.saludar()  # Llamamos al metodo saludar del objeto persona2

persona1.caminar()  # Llamamos al metodo caminar del objeto persona1

persona2.caminar()  # Llamamos al metodo caminar del objeto persona2

print(persona1)  # Imprimimos el atributo nombre del objeto persona1
print(persona2)  # Imprimimos el atributo nombre del objeto persona2


