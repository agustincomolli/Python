# iniciar una lista vacía para contener la entrada del usuario y el valor de la suma de cero.
user_list = []
list_sum = 0

# buscar la entrada del usuario para diez números 
for i in range(10):
    userInput = input("Ingrese cualquier número de 2 dígitos: ")
    
# verifique si el número es par y si es así, agregue a list_sum
# imprimir una advertencia de valor incorrecto cuando se produce una excepción ValueError
    try:
        number = int(userInput)
        user_list.append(number)
        if number % 2 == 0:
            list_sum += number
    except ValueError:
        print("Valor incorrecto. ¡Eso no es un número entero!")

print("user_list: {}".format(user_list))
print("La suma de los números pares en user_list es: {}.".format(list_sum))