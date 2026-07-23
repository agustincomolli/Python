from mylib import clear_screen, color_me, press_enter_to_continue
import csv
import os

clear_screen()
print(color_me("Contruyendo directorios de straming...\n", "yellow"))
with open("./100MostStreamedSongs.csv", mode="r", encoding="UTF-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        # Leer todos los archivos de directorio.
        list_dirs = os.listdir()
        artist = row["Artist(s)"].title()
        song = row["Song"]
        path = os.path.join(artist + "/", song)
    
        if artist not in list_dirs:
            os.mkdir(artist)
        
        file_song = open(path, mode="w", encoding="UTF-8")
        file_song.close()

        print(f"Agregando...{artist} - {song}")

print(color_me("Arbol de directorios completado.\n", "blue"))
press_enter_to_continue()