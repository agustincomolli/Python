import os
import time

def play():
    while True:
        os.system("clear")

        print("Reproduciendo música... 🎵🎶🎵🎶\n")
        print("\n1 - Pausar/Reproducir ⏯️")
        print("2 - Volver al menú ↩️")

        option = input("\nIngrese una opción: ")

        if option == "1":
            print("⏯️")
            time.sleep(2)
        elif option == "2":
            print("⏹️")
            time.sleep(2)
            break


while True:
    os.system("clear")
    
    print("🎵 Reproductor de Música 🎶")
    print("\nPresione 1 para Reproducir ▶️")
    print("Presione 2 para Salir ⏹️")
    print("Presione cualquier otra cosa para volver a ver el menú\n")

    option = input("Ingrese su opción: ")

    if option == "1":
        play()
    elif option == "2":
        break
