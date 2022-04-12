import matplotlib.pyplot as ploter

#valores_x = [1, 2, 3, 4, 5]
#valores_y = [1, 4, 9, 16, 25]

valores_x = list(range(1, 1001))
valores_y = [x ** 2 for x in valores_x]

ploter.scatter(valores_x, valores_y, c=valores_y, cmap=ploter.cm.Blues, 
    edgecolor="none", s=40)

# Establecer el título al gráfico y las etiquetas de los ejes.
ploter.title("Números cuadrados", fontsize=24)
ploter.xlabel("Valores", fontsize=14)
ploter.ylabel("Valores cuadrados", fontsize=14)

# Establecer el tamaño de las etiquetas.
ploter.tick_params(axis="both", which="major", labelsize=14)

ploter.axis([0, 1100, 0, 1100000])

ploter.savefig("28-grafico_dispersion.png", bbox_inches="tight")
ploter.show()
