import os
import time


def color_text(text, color):
    default_color = "\033[0m"
    red_color = "\033[31m"
    green_color = "\033[32m"
    yellow_color = "\033[33m"
    blue_color = "\033[34m"
    magenta_color = "\033[35m"
    cyan_color = "\033[36m"

    if color == "red":
        color = red_color
    elif color == "green":
        color = green_color
    elif color == "blue":
        color = blue_color
    elif color == "yellow":
        color = yellow_color
    elif color == "magenta":
        color = magenta_color
    elif color == "cyan":
        color = cyan_color
    else:
        color = default_color

    return color + text + default_color


def show_interface_1():
    title = color_text("=", "red") + "=" + color_text("=", "blue")
    title += color_text(" App de Música ", "yellow")
    title += color_text("=", "blue") + "=" + color_text("=", "red")

    song = "Radio Gaga"
    artist = color_text("Queen", "yellow")

    prev_control = "PREV"
    next_control = color_text("NEXT", "green")
    pause_control = color_text("PAUSE", "magenta")

    os.system("clear")

    print(f"{title:^120}")

    print(f"\n🔥 ▶️\t{song}")
    print(f"\t{artist}")

    print(f"\n{prev_control:<80}")
    print(f"{next_control:^80}")
    print(f"{pause_control:>80}")


def show_interface_2():
    os.system("clear")

    title = "BIENVENIDO A"
    subtitle = color_text("--    ARMBOOK    --", "blue")
    line_1 = color_text("Definitivamente no es una estafa", "yellow")
    line_2 = color_text("de otro sitio", "yellow")
    line_3 = color_text("de redes sociales", "yellow")
    signature = color_text("Honestamente.", "red")
    username = "Usuario: "
    password = "Contraseña: "

    print(f"{title:^73}")
    print(f"{subtitle:^80}")
    
    print(f"\n{line_1:>80}")
    print(f"{line_2:>80}")
    print(f"{line_3:>80}")
    
    print(f"\n{signature:^80}")

    print(f"\n{username:>38}")
    print(f"{password:>38}")


show_interface_1()
time.sleep(3)
show_interface_2()
