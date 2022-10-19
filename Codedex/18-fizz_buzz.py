"""
Cree un programa fizz_buzz.py que genere números del 1 al 100. 
Aquí está el truco:

Para múltiplos de 3, escriba "Fizz" en lugar del número.
Para múltiplos de 5, escriba "Buzz" en lugar del número.
Aquí está la parte difícil: para múltiplos de 3 y 5, imprime "FizzBuzz".

"""

print("Fizz Buzz 🐝")

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
