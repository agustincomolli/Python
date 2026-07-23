"""
Implementar la clase Queue con dos operaciones básicas:

- put(elemento), que coloca un elemento al final de la cola.
- get(), que toma un elemento del principio de la cola y lo devuelve como 
resultado (la cola no puede estar vacía para realizarlo correctamente).

Sigue las sugerencias:

- Emplea una lista como tu almacenamiento (como lo hicimos con la pila).
put() debe agregar elementos al principio de la lista, mientras que get() debe 
eliminar los elementos del final de la lista.
- Define una nueva excepción llamada QueueError (elige una excepción de la 
cual se derivará) y generala cuando get() intentes operar en una lista vacía.

"""

class QueueError(IndexError):  # Eligir la clase base para la nueva excepción.
    def __init__(self):
        super().__init__("The queue has no elements.")

class Queue:
    def __init__(self):
        self.__queue_list = []

    def put(self, elem):
        self.__queue_list.append(elem)

    def get(self):
        if len(self.__queue_list) > 0:
            first = self.__queue_list[0]
            del self.__queue_list[0]
            return first
        else:
            raise QueueError


que = Queue()
que.put(1)
que.put("perro")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Error de Cola")
    