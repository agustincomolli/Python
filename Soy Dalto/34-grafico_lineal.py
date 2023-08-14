import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data_frame = pd.read_csv("./pedos.csv")
# Generar un gráfico de líneas usando el dataframe.
sns.lineplot(data=data_frame, x="fecha", y="pedos")
# Identificar el punto más alto, de forma manual.
plt.plot("01-09", 17, "o")
# Mostrar el gráfico.
plt.show()