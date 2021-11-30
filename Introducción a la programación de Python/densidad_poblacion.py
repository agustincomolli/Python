# Prueba: función de densidad de población
# Escriba una función nombrada densidad_poblacion que tome dos argumentos poblacion y 
# superficie_area, y devuelva una densidad de población calculada a partir de esos valores. 
# He incluido dos casos de prueba que puede utilizar para verificar que su función 
# funcione correctamente. Una vez que haya escrito su función, use el botón prueba Run para probar su código.

# write your function here
def densidad_poblacion(poblacion, superficie_area):
    return poblacion / superficie_area


# prueba cases for your function
prueba1 = densidad_poblacion(10, 1)
resultado_esperado1 = 10
print("Resultado esperado: {}, resultado actual: {}".format(resultado_esperado1, prueba1))

prueba2 = densidad_poblacion(864816, 121.4)
resultado_esperado2 = 7123.6902801
print("Resultado esperado: {}, resultado actual: {}".format(resultado_esperado2, prueba2))