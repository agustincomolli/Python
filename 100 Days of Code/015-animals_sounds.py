print("*** Sonidos de animales ***\n")
exit = ""

while exit != "s":
    animal = input("¿Qué animal desea? ")
    
    if animal == "gato":
        print("El gato 🐱 hace miaaauuuu")
    elif animal == "perro":
        print("El perro 🐶 hace guau guau!!!")
    elif animal == "vaca":
        print("La vaca 🐮 hace muuuuuu!!")
    elif animal == "pato":
        print("El pato 🦆 hace cuak cuak!")
    elif animal == "cerdo":
        print("El cerdo 🐷 hace oink oink!")
    else:
        print("No tengo más animales.")
    
    exit = input("\n¿Desea salir? [s] ").lower()