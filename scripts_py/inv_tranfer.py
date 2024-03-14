import matplotlib.pyplot as plt
import csv
import numpy as np

# Lista para almacenar los datos
data = []

# Ruta relativa al archivo CSV
csv_file = 'datos_sim/inverter_transfer.ms0.csv'

# Lee el archivo CSV y guarda los datos en la lista, ignorando las primeras dos filas (metadata)
with open(csv_file, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader)  # Saltar la primera fila (metadata)
    next(reader)  # Saltar la segunda fila (encabezado)
    next(reader)
    next(reader)
    for row in reader:
        data.append(row)

# Convierte los datos a arrays de numpy
data = np.array(data, dtype=float)

# Extrae las columnas de datos
x = data[:, 0]
y = data[:, 1]

# Grafica los datos
plt.plot(x, y, label='$I_{sc}$', zorder=1)

# Encuentra los índices más cercanos a x=2 y x=3
idx_2 = np.abs(x - 2).argmin()
idx_3 = np.abs(x - 3).argmin()

# Añade puntos verdes en las coordenadas (2, y[idx_2]) y (3, y[idx_3])
plt.scatter([2, 3], [y[idx_2], y[idx_3]], color=['green', 'red'], zorder=2)

# Etiqueta los valores de y correspondientes con "A" al final
plt.text(2, y[idx_2], f'{y[idx_2]:.4f} A', verticalalignment='bottom', horizontalalignment='right')
plt.text(3, y[idx_3], f'{y[idx_3]:.4f} A', verticalalignment='bottom', horizontalalignment='right')

# Etiquetas de los ejes y título
plt.xlabel('Relación $\\frac{W_P}{W_N}$')
plt.ylabel('Corriente (A)')
plt.title('Corriente de cortocircuito del FO4 en función de la relación $\\frac{W_P}{W_N}$')

# Agrega la leyenda
plt.legend()

# Muestra la cuadrícula
plt.grid(True)

# Elimina el recuadro de la gráfica
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['bottom'].set_visible(True)
plt.gca().spines['left'].set_visible(True)

# Muestra la gráfica
plt.show()
