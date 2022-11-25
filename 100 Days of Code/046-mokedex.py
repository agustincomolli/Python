from mylib import clear_screen, color_me, input_color
import time


mokedex = {}

def print_mokedex():
    """
        DESCRIPTION: Imprime la lista de mokepones.
        
    """
    print()
    for key, value in mokedex.items():
        print(color_me(f"{key.title():^20}", "blue"), end="")
        for subkey, subvalue in value.items():
            print(" | " + f"{subvalue:^20}", end="")
        print()

while True:
    clear_screen()

    print(color_me("🌟 Mokedex 🌟\n", "yellow"))

    name = input_color("Nombre: ", color_input="green")
    type = input_color("Tipo: ", color_input="green")
    attack = input_color("Ataque: ", color_input="green")
    hp = input_color("HP: ", color_input="green")
    mp = input_color("MP: ", color_input="green")
    
    mokedex[name] = {
        "type" : type,
        "attack": attack,
        "hp": hp,
        "mp": mp
    }
    
    print_mokedex()
    time.sleep(2)

    add_again = input_color("\n¿Agregar otro? S|N: ", color_input="green")
    if add_again == "" or add_again.strip().lower()[0] != "s":
        break
