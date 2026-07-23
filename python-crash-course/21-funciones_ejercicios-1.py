# 8-3. Camiseta: Escribe una función llamada make_shirt () que acepte un 
# tamaño y el texto de un mensaje que se debe imprimir en la camiseta. 
# La función debe imprimir una frase que resuma el tamaño de la camiseta 
# y el mensaje impreso en ella. Llame a la función una vez usando argumentos 
# posicionales para hacer una camisa. Llame a la función por segunda vez 
# utilizando argumentos de palabras clave.

# 8-4. Camisas grandes: modifique la función make_shirt () para que las 
# camisas sean grandes por defecto con un mensaje que diga Me encanta Python. 
# Haga una camisa grande y una camisa mediana con el mensaje predeterminado 
# y una camisa de cualquier tamaño con un mensaje diferente.

# 8-5. Ciudades: escriba una función llamada describe_city () que acepte el 
# nombre de una ciudad y su país. La función debe imprimir una oración 
# simple, como Reykjavik está en Islandia. Asigne al parámetro del país un 
# valor predeterminado. Llame a su función para tres ciudades diferentes, 
# al menos una de las cuales no se encuentra en el país predeterminado.

def hacer_camiseta(tamaño="large", mensaje="Me encanta Python"):
    print(f"\nLa camiseta es de tamaño {tamaño} y tiene el siguiente mensaje:\n'{mensaje}'")

hacer_camiseta("small", "Estudiando Python")
hacer_camiseta(mensaje="¡Hola mundo!", tamaño="medium")
hacer_camiseta()

def describir_ciudad(ciudad, pais="Argentina"):
    print(f"{ciudad.title()} está en {pais.title()}")

describir_ciudad("\ncañuelas")
describir_ciudad("madrid", "españa")
describir_ciudad("buenos aires")