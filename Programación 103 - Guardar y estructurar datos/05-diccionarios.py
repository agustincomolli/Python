comidas = {"Agustín":"Cordero","Lorena":"Chocolate", "Carlitos":"Mejillones", "Adrián":"Puma"}

texto = "La comida favorita de"
print(texto, "Adrián es", comidas["Adrián"])
print(texto, "Carlitos es",comidas["Carlitos"])

# Actualizar un valor del diccionario.
comidas.update({"Adrián": "Asado"})
comidas["Lorena"] = "Helado"
print(texto, "Adrián es", comidas["Adrián"])
print(texto, "Lorena es", comidas["Lorena"])

print(comidas)
# Eliminar un item del diccionario.
del comidas["Agustín"]
print(comidas)