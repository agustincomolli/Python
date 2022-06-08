# Programa que muestra un menú para elegir el tipo de sandwitch que desea.

import pyinputplus as pyip

ingredientes = {
                "panes": {
                          "trigo" : 30, 
                          "blanco" : 20, 
                          "masa fermentada": 40
                         },
                 "rellenos": {
                              "pollo" : 50, 
                              "pavo" : 65, 
                              "jamón" : 70,
                              "tofu" : 30
                             },
                 "quesos": {
                            "cheddar" : 30,
                            "mozarella" : 40,
                            "barra" : 20
                           },
                 "aderezos": {
                              "mayonesa" : 10, 
                              "mostaza" : 10, 
                              "lechuga" : 15, 
                              "tomate" : 15
                             }
               }
sandwitch_elegido = {}

def elegir_sandwitch():
    """Muestra varios menú de opciones para la selección de los distintos tipos de 
    ingredientes."""

    pan_elegido = pyip.inputMenu(list(ingredientes["panes"].keys()), 
                                 prompt="¿Qué pan desea?\n", numbered=True)
    sandwitch_elegido["pan"] = {pan_elegido: ingredientes["panes"]
                                             [pan_elegido]}

    relleno_elegido = pyip.inputMenu(list(ingredientes["rellenos"].keys()), 
                                    prompt="\n¿Qué relleno desea?\n", 
                                    numbered=True)
    sandwitch_elegido["relleno"] = {relleno_elegido: ingredientes["rellenos"]
                                                    [relleno_elegido]}

    quiere_queso = pyip.inputYesNo("\n¿Quiere queso? ", yesVal="Sí", noVal="No")
    if quiere_queso == "Sí":
        queso_elegido = pyip.inputMenu(list(ingredientes["quesos"].keys()), 
                                    prompt="\n¿Qué queso desea?\n", 
                                    numbered=True)
        sandwitch_elegido["queso"] = {queso_elegido: ingredientes["quesos"]
                                                     [queso_elegido]}

    quiere_aderezos = pyip.inputYesNo("\n¿Quiere aderezos? ", yesVal="Sí", 
                                    noVal="No")
    if quiere_aderezos == "Sí":
        aderezo_elegido = pyip.inputMenu(list(ingredientes["aderezos"].keys()), 
                                        prompt="\n¿Qué aderezos desea?\n", 
                                        numbered=True)
        sandwitch_elegido["aderezos"] = {aderezo_elegido:
                                         ingredientes["aderezos"][aderezo_elegido]}


def mostrar_seleccion():
    """Muestra la selección del sandwitch."""
    
    total = 0
    print(f"\nSu pedido es:\n{'*' * 13}")
    for item, valor in sandwitch_elegido.items():
        detalle = f"{item.capitalize()}: "
        for subitem, precio in valor.items():
           detalle += f"{subitem.capitalize()} - $ {precio}"
           total += precio
        print(detalle)
    print(f"\nEl total de su pedido es: $ {total * cantidad_sandwitches}")

elegir_sandwitch()
cantidad_sandwitches = pyip.inputInt("\n¿Cuántos sandwitches desea? ", min=1)
mostrar_seleccion()