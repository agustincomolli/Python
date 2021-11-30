# Ejercicio 1:
# ************
# Estamos trabajando con un archivo CSV, que contiene información de 
# los empleados. Cada registro tiene un campo de nombre, seguido de 
# un campo de número de teléfono y un campo de función. El campo 
# del número de teléfono contiene números de teléfono de EE. UU. 
# Y debe modificarse al formato internacional, con "+ 1-" delante 
# del número de teléfono. Complete la expresión regular, usando 
# grupos, para usar la función transform_record para hacer eso.

print("\nEjercicio 1:\n************")

import re
def transform_record(record):
  new_record = re.sub(r"^([\w \.-]*),([\d-]*),([\w \.-]*)",r"\1,+1-\2,\3", record)
  return new_record

print(transform_record("Sabrina Green,802-867-5309,System Administrator")) 
# Sabrina Green,+1-802-867-5309,System Administrator

print(transform_record("Eli Jones,684-3481127,IT specialist")) 
# Eli Jones,+1-684-3481127,IT specialist

print(transform_record("Melody Daniels,846-687-7436,Programmer")) 
# Melody Daniels,+1-846-687-7436,Programmer

print(transform_record("Charlie Rivera,698-746-3357,Web Developer")) 
# Charlie Rivera,+1-698-746-3357,Web Developer

# Ejercicio 2:
# ************
# La función multi_vowel_words devuelve todas las palabras con 3 o más 
# vocales consecutivas (a, e, i, o, u). Complete la expresión regular 
# para hacer eso.

print("\nEjercicio 2:\n************")

import re
def multi_vowel_words(text):
  pattern = r"\w*[aeiou]{3,}\w*"
  result = re.findall(pattern, text)
  return result

print(multi_vowel_words("Life is beautiful")) 
# ['beautiful']

print(multi_vowel_words("Obviously, the queen is courageous and gracious.")) 
# ['Obviously', 'queen', 'courageous', 'gracious']

print(multi_vowel_words("The rambunctious children had to sit quietly and await their delicious dinner.")) 
# ['rambunctious', 'quietly', 'delicious']

print(multi_vowel_words("The order of a data queue is First In First Out (FIFO)")) 
# ['queue']

print(multi_vowel_words("Hello world!")) 
# []

# Ejercicio 3:
# *************
# La función transform_comments convierte los comentarios en un script 
# de Python en los que puede usar un compilador de C. Esto significa 
# buscar texto que comience con una marca de almohadilla (#) y 
# reemplazarlo con barras dobles (//), que es el indicador de comentario 
# de una sola línea en C. Para el propósito de este ejercicio, 
# ignoraremos la posibilidad de una marca de almohadilla incrustada 
# dentro de un comando de Python y asumiremos que solo se usa para 
# indicar un comentario. También queremos tratar las marcas repetitivas 
# (##), (###), etc., como un solo indicador de comentario, para ser 
# reemplazado con solo (//) y no (# //) o (// #) . Complete los 
# parámetros del método de sustitución para completar esta función:

print("\nEjercicio 3:\n************")

import re
def transform_comments(line_of_code):
  result = re.sub(r"[#]{1,}", r"//", line_of_code)
  return result

print(transform_comments("### Start of program")) 
# Should be "// Start of program"
print(transform_comments("  number = 0   ## Initialize the variable")) 
# Should be "  number = 0   // Initialize the variable"
print(transform_comments("  number += 1   # Increment the variable")) 
# Should be "  number += 1   // Increment the variable"
print(transform_comments("  return(number)")) 
# Should be "  return(number)"

# Ejercicio 4:
# ************
# La función convert_phone_number busca un formato de número de teléfono 
# de EE. UU.: XXX-XXX-XXXX (3 dígitos seguidos de un guión, 3 dígitos 
# más seguidos de un guión y 4 dígitos) y lo convierte a un formato 
# más formal que se ve así: (XXX) XXX-XXXX. Complete la expresión 
# regular para completar esta función.

print("\nEjercicio 4:\n************")

import re
def convert_phone_number(phone):
  result = re.sub(r"\b(\d{3})-(\d{3})-(\d{4})\b", r"(\1) \2-\3", phone)
  return result

print(convert_phone_number("My number is 212-345-9999.")) # My number is (212) 345-9999.
print(convert_phone_number("Please call 888-555-1234")) # Please call (888) 555-1234
print(convert_phone_number("123-123-12345")) # 123-123-12345
print(convert_phone_number("Phone number of Buckingham Palace is +44 303 123 7300")) # Phone number of Buckingham Palace is +44 303 123 7300