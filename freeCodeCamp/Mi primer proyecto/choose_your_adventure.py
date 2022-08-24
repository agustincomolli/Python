print("¡Bienvenido a mi primer juego!")

name = input("¿Cuál es tu nombre? ")
age = int(input("¿Cuál es tu edad? "))
health = 10

if age >= 18:
    print("¡Bien! Eres lo suficientemente mayor para jugar.")
    wants_to_play = input("Quieres jugar? [si] ").lower()  # -> Minúsculas.
    if wants_to_play == "si":
        print("¡Juguemos!")

        print(f"Empiezas con {health} de vida ❤️.")

        left_or_right = input("Primera opción... Izquierda o Derecha " +
                              "(👈 izquierda/derecha 👉)? ").lower()

        if left_or_right == "izquierda":
            answer = input("Bien, sigues el camino y llegas a un lago..." +
                           "¿Lo cruzas a nado o das la vuelta alrededor " +
                           "(🏊‍♂️ nadar/rodear 🚶‍♂️)? ").lower()

            if answer == "nadar":
                print("Conseguiste cruzar, pero te mordió un pez 🐟 y " +
                      "perdiste 5 de vida.")
                health -= 5
            elif answer == "rodear":
                print("Diste la vuelta y llegaste al otro lado del lago.")
            else:
                print("😒 No has elegido la opción correcta... De entre la " +
                      "maleza ha salido un oso, te ha atrapado y ahora " +
                      "eres su comida. ¡Perdiste! ☠️")
                exit

            answer = input("Notas que hay una casa y un río. ¿Dónde " +
                           "quieres ir? (🏡 casa/río 🌅) ")
            if answer == "casa":
                print("Vas hacia la casa y su dueño piensa que vas a " +
                      "robarle, busca su escopeta y te recibe a balazos💥. " +
                      "Uno de los perdigones da en tu brazo y pierdes 5 " +
                      "de vida. 🤕")
                health -= 5
                if health == 0:
                    print("Mueres a causa de tus heridas. ¡Perdiste! ☠️")
                else:
                    print("Alguien escucha el disparo de la escopeta y " +
                          "llama a la policía 🚔. Después de un rato dan " +
                          "contigo y eres llevado a un hospital 🏥.")
                    print("Has logrado sobrevivir. ¡Ganaste el juego!")
            else:
                print("Vas hacia el río cuando de repente sale un oso " +
                      "pardo que te estaba siguiendo. No puedes escapar, " +
                      "caes en sus garras y pasas a ser su cena. " +
                      "¡Perdiste! ☠️")
        else:
            print("Caminas unos pasos y te resbalas con una cáscara de " +
                  "banana 🍌, pierdes la estabilidad y caes al suelo " +
                  "golpeando tu cabeza contra una piedra y mueres... " +
                  "¡Perdiste! ☠️")
    else:
        print("Hasta pronto...")
else:
    print("¡No eres lo suficientemente mayor para poder jugar!")
