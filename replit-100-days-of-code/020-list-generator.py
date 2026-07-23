defaul_color = "\033[0m"
yellow_color = "\033[33m"
green_color = "\033[32m"
blue_color = "\033[34m"

print(yellow_color + "*** Generador de Listas ***\n" + defaul_color)
print("Me va a dar un número con el que desea comenzar, un número final" +
      " y cuántos desea que agregue cada vez.\n")

start = int(input("Empezar en: " + green_color))
end = int(input(defaul_color + "Terminar antes de: " + green_color))
increment = int(input(defaul_color + "Incremento entre valores: " +
                      green_color))

print(blue_color)

for i in range(start, end, increment):
    print(i)

print(defaul_color, end="")
