print("💰 BANCO CODEDEX 💰")

pin = int(input("Ingrese el PIN: "))

while pin != 1234:
    pin = int(input("PIN incorrecto. Ingrese el PIN nuevamente: "))

if pin == 1234:
    print("¡PIN aceptado!")
