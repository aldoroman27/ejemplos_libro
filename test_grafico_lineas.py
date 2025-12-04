import numpy as np
import matplotlib.pyplot as plt

# Para crear un gráfico de lineas con matplotlib necesitaremos generar dos arrays que serán los ejes x y y
x = np.linspace(0, 10, 25)
y = np.sin(x) + x/2

#Segundos datos
x2 = np.linspace(0, 10, 25)
y2 = np.cos(x) + x/2

#Graficos de lineas
fig, ax = plt.subplots()
#ax.plot(x, y, lw=4, color="blue") #Cambiando los colores y el grosor de la linea
#ax.plot(x, y, ls=":") # Cambiamos el diseño de una linea continua a una con diseño diferente
#ax.plot(x, y, marker="D", ms=5) # Agregamos marcas a cada par de coordenadas
#ax.plot(x, y, color="red", marker="s", markerfacecolor='black', markeredgecolor='black')#

ax.plot(x, y, marker="o", label="Sin(x) + x/2", color="orange")
ax.plot(x2, y2, marker="o", label="Cos(x) + x/2", color="blue")
ax.legend() 
plt.show()

