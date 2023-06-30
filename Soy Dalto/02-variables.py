# Se declaran y luego se definen.
name = "Agustín"
# |         |----> Definición 
# |
# |--------------> Declaración
# 

# Mostrar datos en la consola.
print("Mostrar datos en la consola".upper())
print(name)
age = 46
print(age)
is_male = True
print(is_male)
# Mostrar un mensaje con el contenido de una variable juntos.
print(f"\nNombre: {name},")
print(f"Edad: {age},")
print(f"¿{name} es hombre?: {is_male}")

# Eliminar variables
del name
del age
del is_male
