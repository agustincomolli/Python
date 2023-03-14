# Convertir de kilómetros a millas y viceversa.
# 1 milla = 1.61 km

def to_miles(km:float):
    """
    Description: Convierte una distancia en kilómetros a millas.
    """
    return km / 1.61


def to_km(miles:float):
    """
    Description: Convierte una distancia de millas a kilómetros.
    """

    return miles * 1.61


kilometers = 12.25
miles = 7.38

miles_to_kilometers = to_km(miles)
kilometers_to_miles = to_miles(kilometers)

print(f"{miles} millas son {round(miles_to_kilometers, 2)} kilómetros.")
print(f"{kilometers} kilómetros son {round(kilometers_to_miles, 2)} millas")