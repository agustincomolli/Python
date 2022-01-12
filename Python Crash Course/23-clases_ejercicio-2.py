# 9-4. Número servido: comience con su programa desde el ejercicio 9-1 
# (página 166). Agregue un atributo llamado number_served con un valor 
# predeterminado de 0. Cree una instancia llamada restaurant de esta clase. 
# Imprima el número de clientes que ha atendido el restaurante y luego 
# cambie este valor e imprímalo nuevamente.
# Agregue un método llamado set_number_served () que le permite establecer 
# el número de clientes que han sido atendidos. Llame a este método con un 
# nuevo número e imprima el valor nuevamente.
# Agregue un método llamado increment_number_served () que le permite 
# incrementar la cantidad de clientes que han recibido servicios. Llame a 
# este método con cualquier número que desee que pueda representar cuántos 
# clientes atendieron, digamos, en un día laboral.

# 9-5. Intentos de inicio de sesión: agregue un atributo llamado 
# login_attempts a su clase de usuario del ejercicio 9-3 (página 166). 
# Escriba un método llamado increment_login_attempts () que incremente el 
# valor de login_attempts en 1. Escriba otro método llamado 
# reset_login_attempts() que restablezca el valor de login_attempts a 0.
# Cree una instancia de la clase User y llame a increment_login_attempts () 
# varias veces. Imprima el valor de login_attempts para asegurarse de que se 
# incrementó correctamente y luego llame a reset_login_attempts (). Imprima 
# login_attempts nuevamente para asegurarse de que se restableció a 0.

print("Ejercicio 9-4:\n" + "*" * 14)

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


mi_restaurante_favorito = Restaurante("La Gran Taberna", "española")
mi_restaurante_favorito.describir_restaurante()
mi_restaurante_favorito.numero_servido = 5
print(f"Clientes atendidos: {mi_restaurante_favorito.numero_servido}")
mi_restaurante_favorito.establecer_numero_servido(10)
print(f"Clientes atendidos: {mi_restaurante_favorito.numero_servido}")
mi_restaurante_favorito.incrementar_numero_servido(3)
print(f"Clientes atendidos: {mi_restaurante_favorito.numero_servido}")
mi_restaurante_favorito.abrir_restaurante()

restaurante_italiano = Restaurante("Campo Di Fiori", "italiana")
restaurante_argentino = Restaurante("La Parrilla", "argentina")

restaurante_argentino.describir_restaurante()
restaurante_italiano.describir_restaurante()


print("Ejercicio 9-5:\n" + "*" * 14)

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


usuario_1 = Usuario("comolli", "agustín", "agustincomolli@yahoo.com.ar")
usuario_1.describir_usuario()
usuario_1.saludar()

usuario_2 = Usuario("mellado", "lorena", "lormelmir@gmail.com")
usuario_2.describir_usuario()
usuario_2.saludar()

for i in range(5):
    usuario_1.incrementar_intentos_inicio()

print(f"El usuario {usuario_1.nombre} ha intentado " +  
    f"{usuario_1.intentos_inicio} veces iniciar sesión.")
usuario_1.reiniciar_intentos_inicio()
print(f"Intentos de inicio de sesión: {usuario_1.intentos_inicio}")