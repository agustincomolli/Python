# Convierte una temperatura de Farenheit a Celsius.
def to_celsius(x):
    return (x - 32) * 5 / 9

for x in range(0, 101, 10):
    print("{:>3} ºF | {:>6.2f} ºC".format(x, to_celsius(x)))

