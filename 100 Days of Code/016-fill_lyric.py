attemps = 0
red_color = "\033[031m"
default_color = "\033[0m"

print("*** Rock Nacional ***")
print("\nCompleta la letra de la canción 🎶")
print("(Escribe la palabra que falta para saber si eres tan bueno como yo.)")

while True:
    attemps +=1

    print("\nY cuando mi _____ esté lista partiré hacia la locura")
    word = input("> ")
    
    if word == "balsa":
        break
    else:
        print(red_color + "\nNo, inténtalo de nuevo." + default_color)

print(f"\n¡Bien hecho! Solo te tomó {attemps} intentos.")