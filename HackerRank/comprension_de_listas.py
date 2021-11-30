if __name__ == '__main__':
    x = int(input("Ingrese x: "))
    y = int(input("Ingrese y: "))
    z = int(input("Ingrese z: "))
    n = int(input("ingrese n: "))
    
    lista= [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i + j + k) != n]
    
    print(lista)
