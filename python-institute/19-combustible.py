"""
Escribir un par de funciones que conviertan l/100km a mpg (milas por galón), 
y viceversa.
1 milla = 1609.344 metros.
1 galón = 3.785411784 litros.
"""


def liters_100km_to_miles_gallon(liters:float):
    """
    Description: Con los litros que se hacen en 100 km devuelve la cantidad
                 de millas que se puede hacer con un galón.
    """
    miles = 100000 / 1609.344
    gallons = liters / 3.785411784
    
    return miles / gallons


def miles_gallon_to_liters_100km(miles:float):
    """
    Description: Convierte de millas x galón a litros x 100km
    """
    one_mile_to_kms = 1609.344 / 1000
    one_gallon_to_liters = 3.785411784
    kms = miles * one_mile_to_kms
    liters =  (100 * one_gallon_to_liters) / kms
    
    return liters


print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
