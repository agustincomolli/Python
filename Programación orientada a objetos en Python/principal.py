#!/usr/bin/env python3

from habitacion import Habitacion
from item import Item
from personaje import Enemigo
from personaje import Amigo
from info_juego import InfoJuego

castillo_espeluznante = InfoJuego("\"El Castillo Espeluznante\"")
castillo_espeluznante.bienvenido()
InfoJuego.info()
InfoJuego.autor = "Agustín =P"

cocina = Habitacion("cocina")
cocina.set_genero("f")
cocina.set_descripcion("Una habitación húmeda y sucia llena de moscas.")

salon_de_baile = Habitacion("salón de baile")
salon_de_baile.set_genero("m")
salon_de_baile.set_descripcion("Una gran sala con adornos dorados en cada pared.")

queso = Item("queso")
queso.set_descripcion("Un bloque de queso grande y maloliente.")
salon_de_baile.set_item(queso)

comedor = Habitacion("comedor")
comedor.set_genero("m")
comedor.set_descripcion("Una amplia habitación con un reluciente suelo de madera; enormes candelabros protegen la entrada.")

libro = Item("libro")
libro.set_descripcion("Un libro realmente bueno titulado 'Tejer para todos'.")
comedor.set_item(libro)

print(f"Hay {Habitacion.numero_habitaciones} para explorar.")

cocina.vincular_habitacion(comedor, "sur")
comedor.vincular_habitacion(cocina, "norte")
comedor.vincular_habitacion(salon_de_baile, "oeste")
salon_de_baile.vincular_habitacion(comedor, "este")

dave = Enemigo("Dave", "Un zombi maloliente")
dave.set_conversacion("Brrlgrh... rgrhl... cerebros...")
dave.set_debilidad("queso")

comedor.set_personaje(dave)

catrina = Amigo("Catrina", "Un esqueleto amigable")
catrina.set_conversacion("¿Por qué hola?")
salon_de_baile.set_personaje(catrina)

habitacion_actual = cocina
mochila = []

muerto = False

while muerto == False:
    print("\n")
    habitacion_actual.get_detalles()
    habitante = habitacion_actual.get_personaje()
    if habitante is not None:
        habitante.describir()

    item = habitacion_actual.get_item()
    if item is not None:
        item.describir()

    comando = input("> ")
    # Comprobar si se escribió una dirección
    if comando in ["norte", "sur", "este", "oeste"]:
        habitacion_actual = habitacion_actual.mover(comando)
    elif comando == "hablar":
        # Hablar con el habitante - ¡Comprobar si hay uno!
        if habitante is not None:
            habitante.hablar()
    elif comando == "pelear":
        # Pelear con el habitante, si lo hay
        if habitante is not None and isinstance(habitante, Enemigo):
            print("¿Con qué lucharás?")
            lucha_con = input()

            if lucha_con in mochila:
                if habitante.pelear(lucha_con) == True:
                    # ¿Qué pasa si ganas?
                    print("¡Hurra, ganaste la pelea!")
                    habitacion_actual.set_personaje(None)
                    if Enemigo.enemigos_a_derrotar == 0:
                        print("¡Felicitaciones, has vencido a la horda enemiga!")
                        muerto = True
                else:
                    # ¿Qué pasa si pierdes?
                    print("\nEl juego ha terminado. \nHas muerto en la pelea.")
                    muerto = True
            else:
                print(f"Tú no tienes {lucha_con} para pelear.")
        else:
            print("No hay nadie aquí con quien pelear")
    elif comando == "abrazar":
        if habitante is not None:
            if isinstance(habitante, Enemigo):
                print("No haría eso si fuera tú ...")
            else:
                habitante.abrazar()
        else:
            print("No hay nadie aquí para abrazar :'(")
    elif comando == "tomar":
        if item is not None:
            if item.genero == "m":
                genero = "el"
            else:
                genero = "la"
            print(f"Pones {genero} {item.get_nombre()} en tu mochila.")
            mochila.append(item.get_nombre())
            habitacion_actual.set_item(None)
    elif comando == "salir":
        break

InfoJuego.creditos()