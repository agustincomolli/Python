# 9-6. Puesto de helados: Un puesto de helados es un tipo específico de 
# restaurante. Escriba una clase llamada IceCreamStand que herede de la 
# clase Restaurante que escribió en el Ejercicio 9-1 (página 166) o el 
# Ejercicio 9-4 (página 171). Cualquiera de las versiones de la clase 
# funcionará; simplemente elige el que más te guste. Agregue un atributo 
# llamado sabores que almacene una lista de sabores de helado. Escribe un 
# método que muestre estos sabores. Cree una instancia de IceCreamStand 
# y llame a este método.

print("Ejercicio 9-6:\n" + "*" * 14)

class Restaurante():
    """Modela un restaurante."""

    def __init__(self, nombre, tipo_cocina) -> None:
        """Inicializar atributos nombre y  tipo de cocina."""
        self.nombre = nombre
        self.tipo_cocina = tipo_cocina
        self.numero_servido = 0

    
    def describir_restaurante(self):
        """Imprime un mensaje con la descripción del restaurante."""
        print(f"Restaurante '{self.nombre}' con cocina {self.tipo_cocina}.")

    
    def abrir_restaurante(self):
        """Muestra un mensaje."""
        print("El restaurante se encuentra abierto al público.")
    

    def establecer_numero_servido(self, numero_servido):
        """Establece el número de clientes atendidos."""
        self.numero_servido = numero_servido

    
    def incrementar_numero_servido(self, clientes):
        """Incrementar la cantidad de clientes que han recibido servicios."""
        self.numero_servido += clientes


class Puesto_de_Helados(Restaurante):
    """Modela una heladería."""
    
    def __init__(self, nombre, tipo_cocina) -> None:
        super().__init__(nombre, tipo_cocina)
        """Inicializar atributos."""
        self.sabores = [
            "dulce de leche", 
            "chocolate", 
            "crema americana", 
            "sambayón"
            ]

    
    def mostrar_sabores(self):
        """Muestra un mensaje con todos los sabores de la heladería."""
        print(f"Nuestros sabores son: {self.sabores}")


heladería = Puesto_de_Helados("Pirulo", "heladería")
heladería.mostrar_sabores()

# 9-7. Admin: Un administrador es un tipo especial de usuario. Escriba una 
# clase llamada Admin que herede de la clase Usuario que escribió en el 
# Ejercicio 9-3 (página 166) o el Ejercicio 9-5 (página 171). Agregue un 
# atributo, privilegios, que almacene una lista de cadenas como "puede 
# agregar una publicación", "puede eliminar una publicación", "puede 
# prohibir a un usuario", etc. Escriba un método llamado show_privileges() 
# que enumere el conjunto de privilegios del administrador. Cree una 
# instancia de Admin y llame a su método.

print("Ejercicio 9-7:\n" + "*" * 14)

class Usuario():
    """Describe un usuario."""

    def __init__(self,apellido, nombre,correo) -> None:
        """Inicializar atributos."""
        self.apellido = apellido
        self.nombre = nombre
        self.correo = correo
        self.intentos_inicio = 0

    
    def describir_usuario(self):
        """Imprime información del usuario en una sola línea."""
        print(f"{self.nombre.capitalize()} {self.apellido.capitalize()} - " + 
            f"{self.correo}")

    
    def saludar(self):
        """Imprime un saludo al usuario."""
        print(f"¡Hola {self.nombre.capitalize()}!")
    

    def incrementar_intentos_inicio(self):
        """Aumenta en 1 la cantidad de intentos de inicio de sesión."""
        self.intentos_inicio += 1

    
    def reiniciar_intentos_inicio(self):
        """Volver a 0 la cantidad de intentos de inicio de sesión."""
        self.intentos_inicio = 0


class Privilegios():
    """Modela los privilegios de un usuario."""

    def __init__(self) -> None:
        """Inicializar atributos."""
        self.privilegios = [
            "puede agregar una publicación",
            "puede eliminar una publicación",
            "puede prohibir a un usuario"
        ]


    def mostrar_privilegios(self):
        """Muestra los privilegios de un usuario administrador."""
        for privilegio in self.privilegios:
            print(f"- {privilegio}.")


class Administrador(Usuario):
    """Modela un usuario administrador."""

    def __init__(self, apellido, nombre, correo) -> None:
        super().__init__(apellido, nombre, correo)
        """Inicializar atributos."""
        self.permisos = Privilegios()
    #     self.privilegios = [
    #         "puede agregar una publicación",
    #         "puede eliminar una publicación",
    #         "puede prohibir a un usuario"
    #     ]


    # def mostrar_privilegios(self):
    #     """Muestra los privilegios de un usuario administrador."""
    #     print(f"{self.nombre.capitalize()} {self.apellido.capitalize()} " + \
    #         f"tiene los siguientes privilegios:")

    #     for privilegio in self.privilegios:
    #         print(f"- {privilegio}.")


usuario_admin = Administrador("comolli", "agustín", "agustincomolli@yahoo.com.ar")
print(f"{usuario_admin.nombre.capitalize()} {usuario_admin.apellido.capitalize()} " + \
    f"tiene los siguientes privilegios:")

usuario_admin.permisos.mostrar_privilegios()

# 9-8. Privilegios: Escriba una clase de Privilegios separada. La clase debe 
# tener un atributo, privilegios, que almacene una lista de cadenas como se 
# describe en el ejercicio 9-7. Mueva el método show_privileges() a esta 
# clase. Cree una instancia de Privilegios como un atributo en la clase 
# Admin. Cree una nueva instancia de Admin y use su método para mostrar 
# sus privilegios.

# 9-9. Actualización de batería: use la versión final de electric_car.py de 
# esta sección. Agregue un método a la clase Batería llamado 
# upgrade_battery(). Este método debería verificar el tamaño de la batería y 
# establecer la capacidad en 85 si aún no lo está. Haga un automóvil 
# eléctrico con un tamaño de batería predeterminado, llame a get_range() una 
# vez y luego llame a get_range() una segunda vez después de actualizar la 
# batería. Debería ver un aumento en el alcance del automóvil.

# Ver archivo: 23-clases_herencia.py