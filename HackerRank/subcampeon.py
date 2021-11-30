#!/usr/bin/env python3

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    puntuaciones = list(arr)[:n]
    campeon = max(puntuaciones)
    
    while max(puntuaciones) == campeon:
        puntuaciones.remove(campeon)
    
    print(max(puntuaciones))