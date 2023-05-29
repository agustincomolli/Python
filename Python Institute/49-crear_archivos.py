from os import strerror

try:
    file = open("new_text.txt", mode="wt", encoding="UTF-8")
    for i in range(10):
        file.write(f"Línea # {i + 1}\n")
    file.close()
except IOError as e:
    print(f"Ocurrió un erro de E/S: {strerror(e.errno)}")