# 9-1. Restaurante: haz una clase llamada Restaurante. El método __init __ () 
# para Restaurant debe almacenar dos atributos: un restaurant_name y un 
# cuisine_type. Cree un método llamado describe_restaurant () que imprima 
# estas dos piezas de información, y un método llamado open_restaurant () 
# que imprima un mensaje indicando que el restaurante está abierto.
# Crea una instancia llamada restaurante de tu clase. Imprima los dos 
# atributos individualmente y luego llame a ambos métodos.

# 9-2. Tres restaurantes: comience con su clase desde el ejercicio 9-1. Cree 
# tres instancias diferentes de la clase y llame a describe_restaurant () 
# para cada instancia.

# 9-3. Usuarios: crea una clase llamada Usuario. Cree dos atributos llamados 
# first_name y last_name, y luego cree varios otros atributos que 
# normalmente se almacenan en un perfil de usuario. Cree un método llamado 
# describe_user () que imprima un resumen de la información del usuario. 
# Cree otro método llamado greet_user () que imprima un saludo personalizado 
# para el usuario.
# Cree varias instancias que representen a diferentes usuarios y llame a 
# ambos métodos para cada usuario.


print("Ejercicio 9-1:\n" + "*" * 14)

class Restaurante():
    """Modela un restaurante."""

    def __init__(self, nombre, tipo_cocina) -> None:
        """Inicializar atributos nombre y  tipo de cocina."""
        self.nombre = nombre
        self.tipo_cocina = tipo_cocina

    
    def describir_restaurante(self):
        """Imprime un mensaje con la descripción del restaurante."""
        print(f"Restaurante '{self.nombre}' con cocina {self.tipo_cocina}.")

    
    def abrir_restaurante(self):
        """Muestra un mensaje."""
        print("El restaurante se encuentra abierto al público.")


mi_restaurante_favorito = Restaurante("La Gran Taberna", "española")
mi_restaurante_favorito.describir_restaurante()
mi_restaurante_favorito.abrir_restaurante()

restaurante_italiano = Restaurante("Campo Di Fiori", "italiana")
restaurante_argentino = Restaurante("La Parrilla", "argentina")

restaurante_argentino.describir_restaurante()
restaurante_italiano.describir_restaurante()

print("Ejercicio 9-3:\n" + "*" * 14)

class Usuario():
    """Describe un usuario."""

    def __init__(self,apellido, nombre,correo) -> None:
        """Inicializar atributos."""
        self.apellido = apellido
        self.nombre = nombre
        self.correo = correo

    
    def describir_usuario(self):
        """Imprime información del usuario en una sola línea."""
        print(f"{self.nombre.capitalize()} {self.apellido.capitalize()} - " + 
            f"{self.correo}")

    
    def saludar(self):
        """Imprime un saludo al usuario."""
        print(f"¡Hola {self.nombre.capitalize()}!")


usuario_1 = Usuario("comolli", "agustín", "agustincomolli@yahoo.com.ar")
usuario_1.describir_usuario()
usuario_1.saludar()

usuario_2 = Usuario("mellado", "lorena", "lormelmir@gmail.com")
usuario_2.describir_usuario()
usuario_2.saludar()