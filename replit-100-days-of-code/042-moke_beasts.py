from mylib import clear_screen, color_me, input_color

moke_beast = {
    "Nombre": None,
    "Tipo": None,
    "Ataque": None,
    "HP": None,
    "MP": None
}


def print_moke_beast():
    color = None

    if moke_beast["Tipo"].lower() == "tierra":
        color = "green"
    elif moke_beast["Tipo"].lower() == "fuego":
        color = "red"
    elif moke_beast["Tipo"].lower() == "agua":
        color = "blue"
    elif moke_beast["Tipo"].lower() == "aire":
        color = ""
    elif moke_beast["Tipo"].lower() == "espíritu":
        color = "magenta"
    else:
        pass

    print()
    for key, value in moke_beast.items():
        print(color_me(f"{key}: {value}", color))


clear_screen()

print(color_me("Moke Beasts 🌱🔥💧💨👻\n", "yellow"))

for key in moke_beast.keys():
    moke_beast[key] = input_color(f"{key}: ", color_input="green").title()

print_moke_beast()
