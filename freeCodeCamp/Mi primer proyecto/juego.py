print("¡Bienvenido a mi primer juego!")

name = input("¿Cuál es tu nombre? ")
age = int(input("¿Cuál es tu edad? "))
health = 10

if age >= 18:
    print("¡Bien! Eres lo suficientemente mayor para jugar.")
    wants_to_play = input("Quieres jugar? [si] ").lower() # -> Minúsculas.
    if wants_to_play == "si":
        print("¡Juguemos!")

        print(f"Empiezas con {health} de vida ❤️.")

        left_or_right = input("Primera opción... Izquierda o Derecha " +
                              "(izquierda/derecha)? ").lower()
        
        if left_or_right == "left":
            answer = input("Bien, sigues el camino y llegas a un lago..." + 
                             "¿Lo cruzas a nado o das la vuelta alrededor " +
                             "(nadar/rodear)? ").lower()
            
            if answer == "nadar":
                print("Diste la vuelta y llegaste al otro lado del lago")
            elif answer == "rodear":
                print("Conseguiste cruzar, pero te mordió un pez 🐟 y " +
                      "perdiste 5 de vida.")
                health -= 5
            else:
                print("😒 No has elegido la opción correcta... De entre la " +
                      "maleza ha salido un oso, te ha atrapado y ahora " +
                      "eres su comida. ¡Perdiste! ☠️")
            

        else:
            print("Te caíste y perdiste... ☠️")
    else:
        print("Hasta pronto...")
else:
    print("¡No eres lo suficientemente mayor para poder jugar!")
