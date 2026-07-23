from mylib import color_me, input_color, clear_screen


class Character:
    name = None
    hp = None # health points
    mp = None # mana points

    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp

    def print_info(self):
        print(color_me("🌟 CHARACTER 🌟\n", "magenta"))
        print(f"Nombre:\t{self.name}")
        print(f"Salud:\t{self.hp} pts.")
        print(f"Maná:\t{self.mp} pts.")


class Player(Character):
    lives = None

    def __init__(self, name, hp, mp, lives):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.lives = lives

    def print_info(self):
        print(color_me("💪 Jugador 💪\n", "blue"))
        print(f"Nombre:\t{self.name}")
        print(f"Salud:\t{self.hp} pts.")
        print(f"Maná:\t{self.mp} pts.")
        print(f"Vidas:\t{self.lives}")
        print(f"¿Estoy vivo? {my_character.am_i_alive().title()}")

    def am_i_alive(self):
        if self.lives > 0:
            return "sí"
        else:
            return "no"


class Enemy(Character):
    type_enemy: str
    strength = None

    def __init__(self, name, hp, mp, type_enemy, strength):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.type_enemy = type_enemy
        self.strength = strength


class Orc(Enemy):
    speed = None

    def __init__(self, name, hp, mp, strength, speed):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.strength = strength
        self.speed = speed
        self.type_enemy = "Orc"

    def print_info(self):
        print(color_me(f"👽 {self.type_enemy} 👽\n", "green"))
        print(f"Nombre:\t{self.name}")
        print(f"Salud:\t{self.hp} pts.")
        print(f"Maná:\t{self.mp} pts.")
        print(f"Fuerza:\t{self.strength} pts.")


class Vampire(Enemy):
    is_it_night = None

    def __init__(self, name, hp, mp, strength, is_it_night):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.type_enemy = "Vampire"
        self.strength = strength
        self.is_it_night = is_it_night

    def print_info(self):
        print(color_me(f"😈 {self.type_enemy} 😈\n", "magenta"))
        print(f"Nombre:\t{self.name}")
        print(f"Salud:\t{self.hp} pts.")
        print(f"Maná:\t{self.mp} pts.")

        if self.is_it_night:
            print("Día/Noche: Noche")
        else:
            print("Día/Noche: Día")


clear_screen()
print(color_me("🌟 Personajes RPG 🌟\n", "yellow"))

my_character = Player("Agnus", 200, 200, 3)
my_character.print_info()
print()

vampire_1 = Vampire("Lestat", 55, 500, 45, True)
vampire_1.print_info()
print()

vampire_2 = Vampire("Drácula", 300, 500, 10, False)
vampire_2.print_info()
print()

orc_1 = Orc("Brutus", 200, 10, 500, 40)
orc_1.print_info()
print()

orc_1 = Orc("Crato", 500, 10, 500, 10)
orc_1.print_info()
print()

orc_1 = Orc("Flatulus", 100, 150, 200, 60)
orc_1.print_info()
print()
