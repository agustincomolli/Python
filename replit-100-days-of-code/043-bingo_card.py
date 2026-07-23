import random
from mylib import clear_screen, color_me, input_color


def generate_list():
    number_list = []
    count = 0
    
    while count < 8:
        number = random.randint(1, 90)
        if number in number_list:
            continue
        number_list.append(number)
        count += 1
    
    number_list.sort()
    
    return number_list


def create_bingo_card():
    bingo_card = []
    number_list = generate_list()

    for i in range(3):
        bingo_card.append([])
        for j in range(3):
            if i == 1 and j == 1:
                bingo_card[i].append("BINGO")
            else:
                bingo_card[i].append(number_list.pop(0))

    return bingo_card


def print_bingo_card():
    clear_screen()

    print(color_me("Generador de tarjetas de Bingo 📅\n", "yellow"))

    for i in range(len(my_bingo_card)):
        for j in range(len(my_bingo_card[i])):
            print(f"{str(my_bingo_card[i][j]):^7}", end="")
            if j < len(my_bingo_card[i]) - 1:
                print("|", end="")
        if i < len(my_bingo_card) - 1:
            print("\n", "-" * 21)

    print("\n")


my_bingo_card = create_bingo_card()

print_bingo_card()
