import pandas as pd

# Obtener los datos del archvio CSV.
data_frame = pd.read_csv("./archivo.csv")
print("Archivo original:")
print(data_frame)

# Mostrar sólo una columna.
print("\nNombres:")
print(data_frame["Nombre"])

# Ordenar los datos.
print("\nArchivo ordenado por edad (Z-A):")
data_frame_sorted = data_frame.sort_values("Edad", ascending=False)
print(data_frame_sorted)

# Concatenar o juntar dos data frames.
data_frame_joined = pd.concat([data_frame, data_frame_sorted])
print(f"\nData frames concatenados:\n{data_frame_joined}")

# Mostrar las dos primeras filas.
print("\nMostrar las dos primeras filas:")
print(data_frame.head(2))

# Mostrar el último elemento del data frame.
print("\nMostrar el último elemento:")
print(data_frame.tail(1))

# Acceder a la cantidad de filas y columnas del data frame.
total_rows, total_columns = data_frame.shape
print(
    f"\n Este data frame tiene {total_rows} filas y {total_columns} columnas.")

# Obtener información estadística del data frame.
data_frame_info = data_frame.describe()
print("\nDescripción del data frame:")
print(data_frame_info)

# Acceder a un dato determinado del data frame.
item_found = data_frame.loc[0, "Nombre"]
print(f"\nItem hallado por loc: {item_found}")

# Acceder al mismo dato pero por los índices.
item_found = data_frame.iloc[0, 0]
print(f"\nItem hallado por iloc: {item_found}")

# Acceder a todos los apellidos.
last_names = data_frame.loc[:, "Apellido"]
print("\nSólo los apellidos:")
print(last_names)

# Obtener los registros cuyas edades sean mayores a 50 años.
oldies = data_frame.loc[data_frame["Edad"] > 50, :]
print("\nPersonas mayores de 50 años:")
print(oldies)
