from os import strerror

try:
    counter = 0
    stream = open("text.txt", mode="rt", encoding="UTF-8")
    char = stream.read(1)
    while char != "":
        print(char, end="")
        counter += 1
        char = stream.read(1)
    
    stream.close()
    print(f"\n\nCaracteres en el archivo: {counter}\n")
except IOError as e:
    print(f"Se produjo un error de E/S: {strerror(e.errno)}")

try:
    char_counter = 0
    line_counter = 0
    stream = open("text.txt", mode="rt", encoding="UTF-8")
    line = stream.readline()
    while line != "":
        line_counter += 1
        for char in line:
            char_counter += 1
            print(char, end="")
        line = stream.readline()

    stream.close()
    print(f"\n\nCaracteres en el archivo: {char_counter}")
    print(f"Líneas en el archvio: {line_counter}\n")
except IOError as e:
    print(f"Se produjo un error de E/S: {strerror(e.errno)}")

try:
    char_counter = 0
    line_counter = 0
    stream = open("text.txt", mode="rt", encoding="UTF-8")
    lines = stream.readlines(20)
    while len(lines) != 0:
        for line in lines:
            line_counter += 1
            for char in line:
                char_counter += 1
                print(char, end="")
        lines = stream.readlines(10)
    stream.close()
    print(f"\n\nCaracteres en el archivo: {char_counter}")
    print(f"Líneas en el archvio: {line_counter}\n")
except IOError as e:
    print(f"Se produjo un error de {strerror(e.errno)}")

try:
    char_counter = 0
    line_counter = 0
    for line in open("text.txt", mode="rt", encoding="UTF-8"):
        line_counter += 1
        for char in line:
            char_counter += 1
            print(char, end="")
    print(f"\n\nCaracteres en el archivo: {char_counter}")
    print(f"Líneas en el archivo: {line_counter}")
except IOError as e:
    print(f"Se produjo un error de E/S: {strerror(e.errno)}")