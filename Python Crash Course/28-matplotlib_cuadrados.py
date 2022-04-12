import matplotlib.pyplot as ploter

valores_entrada = [1, 2, 3, 4, 5]
cuadrados = [1, 4, 9, 16, 25]

ploter.plot(valores_entrada, cuadrados, linewidth=5)

# Establecer el título del gráfico y las etiquetas de los ejes.
ploter.title("Números cuadrados", fontsize=24)
ploter.xlabel("Valores", fontsize=14)
ploter.ylabel("Valores cuadrados", fontsize=14)

# Establecer el tamaño de las etiquetas.
ploter.tick_params(axis="both", labelsize=14)
ploter.show()