print("Ejercicio N° 1:\n" + "*" * 15)
# Cree dos nuevos diccionarios que representen a diferentes personas 
# y almacene los tres diccionarios en una lista llamada personas. 
# Recorra su lista de personas. A medida que recorre la lista, imprima
# todo lo que sepa sobre cada persona.

persona_0 = {
    "nombre" : "agustín",
    "apellido" : "comolli",
    "correo" :  "agustincomolli@yahoo.com.ar"
    }

persona_1 = {
    "nombre" : "adrián",
    "apellido" : "gomez",
    "correo" : "fagomez@yahoo.com.ar"
    }

persona_2 = {
    "nombre" : "gustavo",
    "apellido" : "uhart",
    "correo" : "guhart@hotmail.com."
}

listado = [persona_0, persona_1, persona_2]

for persona in listado:
    print("\nNombre: " + persona["nombre"].title())
    print("Apellido: " + persona["apellido"].title())
    print("Correo: " + persona["correo"].lower())


print("\nEjercicio N° 2:\n" + "*" * 15)
# Mascotas: Haz varios diccionarios, donde el nombre de cada diccionario 
# sea el nombre de una mascota. En cada diccionario, incluya el tipo de 
# animal y el nombre del propietario. Guarde estos diccionarios en una 
# lista denominada mascotas. A continuación, recorra su lista y, a 
# medida que lo hace, imprima todo lo que sabe sobre cada mascota.

mendieta = {"nombre" : "mendieta" , "clase" : "perro", "dueño" : "agustín"}
verdurita = {"nombre" : "verdurita" , "clase" : "tortuga", "dueño" : "antonio"}
boluda = {"nombre" : "boluda" , "clase" : "conejo", "dueño" : "luis"}
gata = {"nombre" : "gata" , "clase" : "gato", "dueño" : "laura"}

mascotas = [mendieta, verdurita, boluda, gata]
for mascota in mascotas:
    print("Nombre: " + mascota["nombre"].title() + ", tipo: " +
        mascota["clase"].title() + ", dueño: " + mascota["dueño"].title())


print("\nEjercicio N° 3:\n" + "*" * 15)
# Lugares favoritos: crea un diccionario llamado lugares_favoritos. 
# Piense en tres nombres para usar como claves en el diccionario y 
# almacene de uno a tres lugares favoritos para cada persona. Para hacer 
# este ejercicio un poco más interesante, pida a algunos amigos que mencionen
#  algunos de sus lugares favoritos. Recorra el diccionario e imprima el 
# nombre de cada persona y sus lugares favoritos.
lugares_favoritos = {
    "agustín" : ["tandil", "navarra", "san luís"],
    "lorena" : ["esquina", "andalucía", "salta"],
    "adrián" : ["san luís", "punta cana", "mendoza"]
    }

for nombre, lugares in lugares_favoritos.items():
    print("\nLugares favoritos de " + nombre.title() + ":")
    for lugar in lugares:
        print("\t" + lugar.title())

print("\nEjercicio N° 3:\n" + "*" * 15)
# Ciudades: haz un diccionario llamado ciudades. Utilice los nombres 
# de tres ciudades como claves en su diccionario. Cree un diccionario 
# de información sobre cada ciudad e incluya el país en el que se 
# encuentra la ciudad, su población aproximada y un dato sobre esa 
# ciudad. Las claves del diccionario de cada ciudad deben ser algo 
# como país, población y hechos. Imprime el nombre de cada ciudad y 
# toda la información que tengas almacenada sobre ella.
ciudades = {
    "cañuelas" : {
        "país" : "argentina",
        "población" : 31901,
        "dato" : "aquí nació el dulce de leche."
     },
    "pamplona" : {
        "país" : "españa",
        "población" : 199066,
        "dato" : "en la Mandarra de la Ramos se come muy bien."
        },
    "san luís" : {
        "país" : "argentina",
        "población" : 298069,
        "dato" : "en la catedral está enterrado juan pascual pringles."
        }
    }

for ciudad, datos in ciudades.items():
    print("\n" + ciudad.title() + ":")
    print("\t País: " + datos["país"].title())
    print("\t Población: " + str(datos["población"]))
    print("\t Dato: " + datos["dato"].capitalize())