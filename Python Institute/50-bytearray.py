from os import strerror

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 + i

try:
    file = open("file.bin", mode="wb")
    file.write(data)
    file.close()
except IOError as e:
    print(f"Ocurrió un error de E/S: {strerror(e.errno)}")


try:
    file = open("file.bin", mode="rb")
    file.readinto(data)
    file.close()
    for byte in data:
        print(hex(byte), end="")
except IOError as e:
    print(f"Ocurrió un error de E/S: {strerror(e.errno)}")