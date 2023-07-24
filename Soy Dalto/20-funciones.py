# Crear una función simple.
def greet_me():
    print("¡Hola! ¿Cómo estás?")


# Crear una función que tenga parámetros.
def greet(name: str):
    print(f"¡Hola, {name}! ¿Cómo estás?")


# Crear una función que retorne valores.
def create_password(number: int):
    # Crear una lista con las letras del alfabeto.
    letters = [chr(char_number) for char_number in range(97, 123)]
    # Tomar el primer número del argumento.
    number = str(number)
    number = int(number[0])
    # Generar los índices para crear las contraseñas.
    index_1 = number - 2
    index_2 = number
    index_3 = number - 5
    # Crear la contraseña con los índices generados.
    password = f"{letters[index_1]}{letters[index_2]}{letters[index_3]}{number**3}"

    return password


# Crear una función con parámetros con valores predeterminados.
def say_name(first_name, last_name, prefix=""):
    return f"{prefix} {first_name} {last_name}"


greet_me()
greet("Lorena")
my_password = create_password(23)
print(my_password)
print(say_name("Agustín", "Comolli", "Sr."))