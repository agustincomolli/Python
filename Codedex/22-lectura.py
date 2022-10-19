"""
Cree un programa de lectura.py que almacene los siguientes elementos en una 
lista books:

"Zero to One"
"The Lean Startup"
"The Mom Test"
"Made to Stick"
"Life in Code"

Imprima la lista para asegurarse de que no haya ningún error.

Supongamos que queremos añadir un libro más a la lista: "Zero to Sold". 
¿Puedes usar un método de lista para hacerlo?

Digamos que terminamos de leer "Zero to One"y "The Lean Startup". 
¿Puedes usar el .remove()método para eliminar uno y el .pop()método para 
eliminar el otro?

¡Imprima la lista actualizada para asegurarse de que todo esté listo!

"""

books = [
    "Zero to One",
    "The Lean Startup",
    "The Mom Test",
    "Made to Stick",
    "Life in Code",
]

print("Club de libros 📖\n")

print(f"Lista de libros: {books}")

books.append("Zero to Sold")

books.remove("Zero to One")
books.pop(0)

print(f"Lista actualizada: {books}")
