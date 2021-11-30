# Convertir un valor de temperatura Farenheit en Celsius.
# Fórmula (32 °F − 32) × 5/9 = 0 °C
print("Convertidor de Temperaturas\n" + "=" * 27)
fahrenheit = int(input("\nTemperatura en °F: "))
celsius = (fahrenheit - 32) * 5/9 # Da un valor float.
celsius = int(celsius)
print("Temperatura en °C: " + str(celsius) +"\n")