import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data_frame = pd.read_csv("./datos_boxplot.csv")
# Generar un gráfico de dispersión.
sns.boxplot(data=data_frame, x="categoría", y="valor")
# Mostrar el gráfico.
plt.show()