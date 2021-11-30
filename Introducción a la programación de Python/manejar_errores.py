def party_planner(galletitas, personas):
    sobras = None
    cant_x_persona = None
    # TODO: Agregue un bloque try-except aquí para 
    #       asegurarse de que no ocurra ZeroDivisionError..
    try:
        cant_x_persona = galletitas // personas
        sobras = galletitas % personas
    except ZeroDivisionError:
        print("La cantidad de personas debe ser mayor a 1.")
    return(cant_x_persona, sobras)

# El bloque de código principal está debajo; no edites esto
vamos_de_fiesta = 's'
while vamos_de_fiesta == 's':

    galletitas = int(input("¿Cuántas galletas estás horneando? "))
    personas = int(input("¿Cuántas personas asistirán? "))

    galletitas_x_persona, sobras = party_planner(galletitas, personas)

    if galletitas_x_persona:  # if galletitas_x_persona is not None
        mensaje = "\n¡Vamos de fiesta! Tendremos {} asistentes, cada uno podrá comer {} galletas y nos sobrarán {}."
        print(mensaje.format(personas, galletitas_x_persona, sobras))

    vamos_de_fiesta = input("\n¿Te gustaría festejar más? (s o n) ")