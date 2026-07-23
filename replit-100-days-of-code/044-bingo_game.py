from mylib import clear_screen, color_me, input_color


def create_unique_numbers():
    """
        DESCRIPTION: Genera un lista de 8 número aleatorios sin repetir
                     ordenados de menor a mayor.
    """
    from random import randint

    number_list = []
    count = 0

    while count < 8:
        random_number = randint(1, 90)
        if random_number in number_list:
            continue
        number_list.append(random_number)
        count += 1

    number_list.sort()
    return number_list


def create_bingo_card():
    new_bingo_card = []
    number_list = create_unique_numbers()

    for row in range(3):
        new_bingo_card.append([])
        for col in range(3):
            if row == 1 and col == 1:
                new_bingo_card[row].append("BINGO")
            else:
                new_bingo_card[row].append(number_list.pop(0))

    return new_bingo_card


def print_bingo_card():
    clear_screen()

    print(color_me(f"{'Juego de Bingo! 📅':^33}\n", "yellow"))

    for row in range(len(bingo_card)):
        for col in range(len(bingo_card[row])):
            print(f"{str(bingo_card[row][col]):^10}", end="")
            if col < len(bingo_card[row]) - 1:
                print("|", end="")
        if row < len(bingo_card) - 1:
            print("\n", "-" * 30)

    print("\n")


def check_number(number:int):
    for row in range(len(bingo_card)):
        for col in range(len(bingo_card[row])):
            if number == bingo_card[row][col]:
                bingo_card[row][col] = "X"
                return 1
    return 0


bingo_card = create_bingo_card()
wins = 0
while wins < 8:
    print_bingo_card()
    number = int(input("\n¿Qué número salió? "))
    wins += check_number(number)
    print_bingo_card()
print(color_me(f"\n{'¡BINGO! Ganaste 🤑🤑🤑':^30}", "cyan"))