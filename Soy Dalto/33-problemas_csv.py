"""
Ejercicio: Cambiar el tipo de dato de una columna en un data frame.

"""
import pandas as pd


def view_data(data_frame, title):
    print(f"{title}: \n{data_frame}")


# Obtener el data frame.
data_frame = pd.read_csv("./archivo.csv")

view_data(data_frame, "DataFrame original:")

# Convertir el tipo de dato de una columna.
data_frame["Edad"] = data_frame["Edad"].astype("str")
print("\nEl nuevo tipo de dato de la columna 'Edad' es:"
      + f"{type(data_frame['Edad'][0])}")

# Reemplazar un valor del data_frame.
data_frame["Nombre"].replace("María Eugenia", "Hermana María", inplace=True)
view_data(data_frame, "\nDataFrame con nombre reemplazado:")

# Eliminar filas con datos faltantes.
data_frame = data_frame.dropna()
view_data(data_frame, "\nDataFrame sin filas con datos faltantes:")

# Eliminar filas repetidas.
data_frame = data_frame.drop_duplicates()
view_data(data_frame, "\nDataFrame sin filas repetidas:")

# Crear una copia del archivo CSV limpiado anteriormente.
data_frame.to_csv("./archivo_limpio.csv")