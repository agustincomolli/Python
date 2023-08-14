import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data_frame = pd.read_csv("./ingresos.csv", encoding="UTF-8")
# Generar un gráfico de barras.
sns.barplot(data=data_frame, x="fuente", y="ingresos")
# Mostrar el total de ingresos.
print(f"El total de los ingresos es de u$s {data_frame['ingresos'].sum()}")
plt.show()