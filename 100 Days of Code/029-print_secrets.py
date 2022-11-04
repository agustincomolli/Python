import os


def print_color(word, color):
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

    print(color, word, default_color, sep="", end="")


print("Super Print Color\n")
print("Con mi ", end="")
print_color("nuevo programa", "magenta")
print_color(", solo puedo llamar rojo (\"y\") ", "")
print_color("y ", "red")
print_color("esa palabra aparecerá en el color que configuré.", "")
print_color("\n\nSin ", "")
print_color("espacios extraños", "cyan")
print_color(".\n\nÉpico", "")