"""
Extender ligeramente las capacidades de la clase Queue. Queremos que tenga un 
método sin parámetros que devuelva True si la cola está vacía y False de lo 
contrario.

Completa el código que te proporcionamos en el editor. Ejecútalo para 
comprobar si genera un resultado similar al nuestro.

"""


class QueueError(IndexError):  # Eligir la clase base para la nueva excepción.
    def __init__(self):
        super().__init__("The queue has no elements.")


class Queue:
    def __init__(self):
        self.queue_list = []

    def put(self, elem):
        self.queue_list.append(elem)

    def get(self):
        if len(self.queue_list) > 0:
            first = self.queue_list[0]
            del self.queue_list[0]
            return first
        else:
            raise QueueError


class SuperQueue(Queue):
    def is_empty(self):
        return len(self.queue_list) == 0


que = SuperQueue()
que.put(1)
que.put("perro")
que.put(False)
for i in range(4):
    if not que.is_empty():
        print(que.get())
    else:
        print("Cola vacía")
