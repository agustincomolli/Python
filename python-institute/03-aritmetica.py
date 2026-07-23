# 3 por x al cubo, menos 2 por x al cuadrado, más 3 por x, menos 1

def aritmetics(x:int):
    x = float(x)
    result = 3 * (x**3) - 2 * (x**2) + 3 * x - 1
    
    return result


test = 0
print("Resultado: ", aritmetics(test))
test = 1
print("Resultado: ", aritmetics(test))
test = -1
print("Resultado: ", aritmetics(test))