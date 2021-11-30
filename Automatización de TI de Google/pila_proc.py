# Ejemplo de la implementación de una pila con el enfoque de programación
# procedimental.-
pila = []

def push(val):
    pila.append(val)

def pop():
    valor = pila[-1]
    del pila[-1]
    return valor

push(3)
push(2)
push(1)

print(pop())
print(pop())
print(pop())