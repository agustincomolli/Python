import random

rachas = 0

def crear_lista():
    """Crear lista aleatoria que simula el lanzamiento de una moneda.
    De vuelve 0 si es cara, 1 si es seca."""
    monedas_lanzadas = []
    for i in range(100):
        monedas_lanzadas.append(random.randint(0, 1))
    return monedas_lanzadas


def comprobar_coincidencias(monedas_lanzadas):
    """Verificar si hay una racha de 6 números iguales en la lista."""
    coincidencias = 0
    for i in range(len(monedas_lanzadas)-7):
        if ([0,0,0,0,0,0] == monedas_lanzadas[i:i + 6]) or \
            ([1,1,1,1,1,1] == monedas_lanzadas[i:i + 6]):
            coincidencias = 1
            break
    return coincidencias


for experimento in range(10000):
    monedas_lanzadas = crear_lista()
    rachas += comprobar_coincidencias(monedas_lanzadas)

print(rachas)
print('Posibilidad de racha: %s%%' % (rachas / 100))