"""
Defina una playlistlista y agregue algunas canciones. Por ejemplo:

# 💿 Theme: Indie Travel Songs

playlist = [
   "Porches - rangerover",
   "Mount Eerie - You Swan, Go On",
   "Carolyn Polachek - Look at Me Now",
   "Pinegrove - Darkness"
   "LVP UP - Spirit Was",
   "Mitski - First Love / Late Spring",
]
¡Ahora recorra la lista e imprima todo!

Pruebe diferentes formas de hacerlo antes de continuar.

"""

playlist = [
    "Porches - rangerover",
    "Mount Eerie - You Swan, Go On",
    "Carolyn Polachek - Look at Me Now",
    "Pinegrove - Darkness"
    "LVP UP - Spirit Was",
    "Mitski - First Love / Late Spring",
]

print("💿 Theme: Indie Travel Songs")

for song in playlist:
    print(f"- {song}")

print("\nOtra forma: ")

for i in range(len(playlist)):
    print(f"{i} - {playlist[i]}")