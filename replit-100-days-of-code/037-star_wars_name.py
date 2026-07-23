import os
import time
from mylib import color_me, input_color


def get_new_name(first_name: str, last_name: str, moms_last_name: str,
                 city_born: str):

    new_name = f"{first_name[:3]}{last_name[:3]} "
    new_name += f"{moms_last_name[:2]}{city_born[-3:]}"

    return new_name.title()


os.system("clear")

print(color_me("🌟 Tu nombre de STAR WARS 🌟\n", "yellow"))

user_data = input_color("Ingresa tu nombre, apellido, el apellido de soltera " +
                        "de tu mamá y tu ciudad de nacimiento. Todo separado por espacios.\n\n> ",
                        color_input="green").split()

star_wars_name = get_new_name(user_data[0], user_data[1], user_data[2],
                              user_data[len(user_data) - 1])

print("\n👉 Tu nombre es: " + color_me(star_wars_name, "blue"))
