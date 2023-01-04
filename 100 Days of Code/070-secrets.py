from mylib import *
import os

# Crear variables de entorno para guardar los nombres de usuario y contraseñas.
os.environ["user_name"] = "agustincomolli"
os.environ["user_pass"] = "user123"

while True:
    clear_screen()
    print(color_me("🌟 Inicio de sesión 🌟\n", "yellow"))
    user = input_color("Usuario: ", "green")
    password = input_color("Contraseña: ", "green")
    if user == os.environ["user_name"] and password == os.environ["user_pass"]:
        print(color_me("Hola Agustín, bienvenido.", "blue"))
        break
    else:
        show_error("Usuario o contraseña inválida, inténtelo de nuevo.")

os.environ.pop("user_name")
os.environ.pop("user_pass")