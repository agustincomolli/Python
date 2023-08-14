import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data_frame = pd.read_csv("./datos_grafico_dispersion.csv")
# Generar un gráfico de dispersión.
sns.scatterplot(data=data_frame, x="tiempo", y="dinero")
# Mostrar el gráfico.
plt.show()