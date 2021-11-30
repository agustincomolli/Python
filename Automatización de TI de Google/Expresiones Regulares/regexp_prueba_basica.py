# Prueba de práctica: Expresiones regulares básicas

# Ejercicio 1
# La función check_web_address verifica si el texto pasado califica
# como una dirección web de nivel superior, lo que significa que contiene 
# caracteres alfanuméricos (que incluyen letras, números y guiones bajos), 
# así como puntos, guiones y un signo más, seguidos de un punto. y un 
# dominio de nivel superior solo de caracteres, como ".com", ".info", 
# ".edu", etc. Complete la expresión regular para hacerlo, utilizando 
# caracteres de escape, comodines, calificadores de repetición, principio 
# y fin caracteres de línea y clases de caracteres.

import re
def check_web_address(text):
  pattern = r"^[\w .\- \+]*[com org info edu US]$"
  result = re.search(pattern, text)
  return result != None

print("\nEjercicio 1:\n************")
print(check_web_address("gmail.com")) # True
print(check_web_address("www@google")) # False
print(check_web_address("www.Coursera.org")) # True
print(check_web_address("web-address.com/homepage")) # False
print(check_web_address("My_Favorite-Blog.US")) # True

# Ejercicio 2
# La función check_time comprueba el formato de hora de un reloj de 12 
# horas, de la siguiente manera: la hora está entre 1 y 12, sin cero a 
# la izquierda, seguida de dos puntos, luego minutos entre 00 y 59, 
# luego un espacio opcional y luego AM o PM, en mayúsculas o minúsculas. 
# Complete la expresión regular para hacer eso. ¿Cuántos de los conceptos 
# que acaba de aprender puede usar aquí?
import re
def check_time(text):
  pattern = r"^[1]?[0-9]:[0-5][0-9][\s]?[aApP][mM]$"
  result = re.search(pattern, text)
  return result != None

print("\nEjercicio 2:\n************")
print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:60am")) # False
print(check_time("five o'clock")) # False

# Ejercicio 3
# La función contiene_acrónimo comprueba en el texto la presencia de 2 
# o más caracteres o dígitos entre paréntesis, con al menos el primer 
# carácter en mayúsculas (si es una letra), devolviendo True si se 
# cumple la condición, o False en caso contrario. Por ejemplo, 
# "La mensajería instantánea (IM) es un conjunto de tecnologías de 
# comunicación que se utilizan para la comunicación basada en texto" 
# debe devolver True ya que (IM) satisface las condiciones de 
# coincidencia ". Complete la expresión regular en esta función:
import re
def contains_acronym(text):
  pattern = r"\([A-Z0-9]?.*\)" 
  result = re.search(pattern, text)
  return result != None

print("\nEjercicio 3:\n************")
print(contains_acronym("Instant messaging (IM) is a set of communication technologies used for text-based communication")) # True
print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication")) # True
print(contains_acronym("Please do NOT enter without permission!")) # False
print(contains_acronym("PostScript is a fourth-generation programming language (4GL)")) # True
print(contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!")) # True

# Ejercicio 4
# Complete el código para verificar si el texto transmitido incluye 
# un posible código postal de EE. UU., Con el siguiente formato: 
# exactamente 5 dígitos y, a veces, pero no siempre, seguido de un 
# guión con 4 dígitos más. El código postal debe estar precedido por 
# al menos un espacio y no puede estar al comienzo del texto.
import re
def check_zip_code (text):
  result = re.search(r"\s\d{5}[-\d{4}]{0,1}", text)
  return result != None

print("\nEjercicio 4:\n************")
print(check_zip_code("The zip codes for New York are 10001 thru 11104.")) # True
print(check_zip_code("90210 is a TV show")) # False
print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001.")) # True
print(check_zip_code("The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9.")) # False