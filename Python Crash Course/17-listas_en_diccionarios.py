# Almacenar información sobre la pizza pedida.
pizza = {
    "masa" : "de molde",
    "ingredientes" : ["muzzarella", "anchoas"]
    }

# Mostrar el pedido.
print("Usted pidió una pizza " + pizza["masa"] + " con los siguientes" +
    " ingredientes:")
for ingrediente in pizza["ingredientes"]:
    print("\t" + ingrediente)


lenguajes_favoritos = {
    "Agustín" : ["Clipper", "Visual Basic", "Python"],
    "Gustavo" : ["Turbo Pascal", "COBOL"],
    "Carlitos" : ["Turbo Pascal", "Visual Basic"]
}

for nombre, lenguajes in lenguajes_favoritos.items():
    print("\nLos lenguajes de programación favoritos de " + nombre + " son:")
    for lenguaje in lenguajes:
        print("\t" + lenguaje)