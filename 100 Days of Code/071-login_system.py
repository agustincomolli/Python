from mylib import *
import random


def create_user():
    """
    Description: Crea un usuario con su nombre de usuario, contraseña
                 encriptada, y un número de 4 dígitos para fortalecer la 
                 contraseña.
    Return:      Diccionario.
    """
    clear_screen()
    print(color_me("👧 Nuevo usuario 🧑\n"))
    username = input_color("Nombre de usuario: ", "green")
    password = input_color("Contraseña: ", "green")
    # Fortalecer la contraseña agregando un número aleatorio de 4 dígitos.
    salt = random.randint(1000, 9999)
    password = f"{password}{salt}"
    # Encriptar la contraseña.
    password = hash(password)

    user = {
        username: {
            "password": password,
            "salt": salt
        }
    }

    return user


def login(user_dict: dict):
    """
    Description: Pide los datos de usuario y chequea si es correcto
                 el nombre y su contraseña.
    Parameters: 
                 - user_dict: Diccionario con todos los usuarios registrados.
    Return:      Devuelve el nombre se usuario si todo es correcto, sino
                 devuelve un valor None y un mensaje con el error 
                 correspondiente.
    """
    clear_screen()
    print(color_me("🌟 Iniciar Sesión 🌟\n"))
    username = input_color("Nombre de usuario: ", "green")
    password = input_color("Contraseña: ", "green")
    
    if username in user_dict:
        # Obtener el código que fortaleció la contraseña del usuario.
        salt = user_dict[username]["salt"]
        # Encriptar la contraseña ingresada junto al código salt.
        hashed_pass = hash(f"{password}{salt}")
        # Comparar si la contraseña hasheada es igual a la que está guardada.
        if hashed_pass == user_dict[username]["password"]:
            return username, ""
        else:
            return None, "La contraseña es inválida."
    else:
        return None, "El usuario no existe."


user_dict = {}

while True:
    clear_screen()
    title = color_me("🔐 Seguridad 🔐", "yellow")
    options = ["Nuevo usuario", "Iniciar sesión", "Salir"]
    # Mostrar menú de opciones.
    selected_option = choose_option(title, options, "green")

    if selected_option == 1:
        user_dict.update(create_user())
    elif selected_option == 2:
        user, message = login(user_dict)
        clear_screen()
        if user != None:
            print(color_me(f"Bienvenido {user}\n", "blue"))
        else:
            show_error(message)
        press_enter_to_continue()
    if selected_option == 3:
        break
