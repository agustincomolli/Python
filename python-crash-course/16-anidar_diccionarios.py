alien_0 = {"color" : "verde", "puntos" : 5}
alien_1 = {"color" : "amarillo", "puntos" : 10}
alien_2 = {"color" : "rojo", "puntos" : 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# Crear una lista para almacenar aliens.
aliens = []

# Crear 30 aliens.
for i in range(30):
    nuevo_alien = {"color" : "verde", "puntos" : 5, "velocidad" : "lenta"}
    aliens.append(nuevo_alien)

for alien in aliens[:3]:
    if alien["color"] == "verde":
        alien["color"] = "amarillo"
        alien["puntos"] = 10
        alien["velocidad"] = "media"
    elif alien["color"] == "amarillo":
        alien["color"] = "rojo"
        alien["puntos"] = 15
        alien["velocidad"] = "rápida"


# Mostrar los 5 primeros aliens.
for alien in aliens[:5]:
    print(alien)

print("...")

# Mostrar cuántos nuevos aliens se han creado.
print("Número total de aliens: " + str(len(aliens)))