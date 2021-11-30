# Listas
print("Listas:\n" + "=" * 7)

lst_nombres = []
lst_nombres = ["Lorena", "Adrián", "Marcela"]
lst_nombres.append("Carlitos")
lst_nombres.insert(0, "Agustín")
print(lst_nombres)
print(f"Tercer valor de la lista: {lst_nombres[2]}")

# Diccionarios
print("\nDiccionarios:\n" + "=" * 13)
dic_usuario = {}
dic_usuario["Nombre"] = "Agustín"
dic_usuario["Apellido"] = "Comolli"
dic_usuario["Correo"] = "agustincomolli@yahoo.com.ar"
print(dic_usuario)
print(f"Correo electrónico: {dic_usuario['Correo']}")

# Listas de diccionarios
print("\nListas de diccionarios:\n" + "=" * 23)
dic_agustin = {}
dic_agustin["Nombre"] = "Agustín"
dic_agustin["Apellido"] = "Comolli"
dic_Lorena = {}
dic_Lorena["Nombre"] = "Lorena"
dic_Lorena["Apellido"] = "Mellado"

lst_matrimonio = []
lst_matrimonio.append(dic_agustin)
lst_matrimonio.append(dic_Lorena)
print(lst_matrimonio)
print(f"{lst_matrimonio[0]['Nombre']} y {lst_matrimonio[1]['Nombre']}")
