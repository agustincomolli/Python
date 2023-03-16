import re


def input_email(message):
    """
    Pide al usuario que ingrese un email y valida la entrada.

    Args:
    message (str): mensaje a mostrar al usuario al pedir el email.

    Returns:
    str: email válido ingresado por el usuario.
    """
    # Expresión regular para validar un email
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

    # Pedimos al usuario que ingrese un email
    email = input(message)

    # Validamos la entrada del usuario
    while not re.match(pattern, email):
        print("\nEmail inválido, ingrese un email válido")
        email = input(message)

    return email


def input_date(message):
    """
    Pide al usuario que ingrese una fecha en formato dd/mm/yyyy y valida la entrada.

    Args:
    message (str): mensaje a mostrar al usuario al pedir la fecha.

    Returns:
    str: fecha válida en formato dd/mm/yyyy ingresada por el usuario.
    """
    # Expresión regular para validar una fecha en formato dd/mm/yyyy
    pattern = r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/([0-9]{4})$"

    # Pedimos al usuario que ingrese una fecha
    date = input(message)

    # Validamos la entrada del usuario
    while not re.match(pattern, date):
        print("Fecha inválida, ingrese una fecha válida en formato dd/mm/yyyy")
        date = input(message)

    return date


def input_number(message):
    """
    Pide al usuario que ingrese un número y valida la entrada.

    Args:
    message (str): mensaje a mostrar al usuario al pedir el número.

    Returns:
    int: número válido ingresado por el usuario.
    """
    # Pedimos al usuario que ingrese un número
    number = input(message)

    # Validamos la entrada del usuario
    while not number.isdigit():
        print("Ingreso inválido, ingrese un número válido")
        number = input(message)

    return int(number)


def input_yes_no(message):
    """
    Pide al usuario que ingrese una entrada sí o no y valida la entrada.

    Args:
    message (str): mensaje a mostrar al usuario al pedir la entrada.

    Returns:
    bool: 'True' o 'False' según la entrada del usuario.
    """
    while True:
        # Pedimos al usuario que ingrese una entrada sí o no
        response = input(message)

        # Validamos la entrada del usuario
        if response.lower() == "s":
            return True
        elif response.lower() == "n":
            return False
        else:
            print("Por favor ingrese 's' o 'n'.")


def input_password(message):
    """
    Solicita una contraseña al usuario y la valida para asegurarse de que cumple con los siguientes requisitos:
      - Tiene al menos 8 caracteres
      - Tiene al menos un dígito
      - Tiene al menos una mayúscula
      - Tiene al menos una minúscula
    Mientras el usuario escribe la contraseña, se muestran asteriscos en lugar de los caracteres ingresados.
    """
    import getpass

    while True:
        password = getpass.getpass(message)
        if len(password) < 8:
            print(
                "La contraseña debe tener al menos 8 caracteres. Por favor, inténtelo de nuevo.")
        elif not any(char.isdigit() for char in password):
            print(
                "La contraseña debe tener al menos un dígito. Por favor, inténtelo de nuevo.")
        elif not any(char.isupper() for char in password):
            print(
                "La contraseña debe tener al menos una mayúscula. Por favor, inténtelo de nuevo.")
        elif not any(char.islower() for char in password):
            print(
                "La contraseña debe tener al menos una minúscula. Por favor, inténtelo de nuevo.")
        else:
            return password


def input_int_range(message, min_value, max_value):
    """
    DESCRIPTION: Muestra un mensaje al usuario y solicita un número entero en 
                 un rango especificado.
    PARAMETERS:
                - message: El mensaje a mostrar al usuario.
                - min_value: El valor mínimo permitido para el número.
                - max_value: El valor máximo permitido para el número.
    RETURNS:    El número entero seleccionado por el usuario.
    """
    while True:
        # Solicita al usuario que introduzca un número
        value = input(message)

        # Verifica que el número sea un entero y esté en el rango especificado
        if value.isdigit() and int(value) >= min_value and int(value) <= max_value:
            return int(value)
        else:
            print("Valor inválido, intente de nuevo.")
