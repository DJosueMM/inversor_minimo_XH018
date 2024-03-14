import matplotlib.pyplot as plt
import csv

# Lista para almacenar los datos
data = []

# Ruta relativa al archivo CSV
csv_file = 'datos_sim/f04__70C.csv'

# Lee el archivo CSV y guarda los datos en la lista, ignorando la segunda fila (encabezado)
with open(csv_file, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader)  # Saltar la primera fila (metadata)
    next(reader)  # Saltar la segunda fila (encabezado)
    for row in reader:
        data.append(row)

# Convierte los datos a arrays de numpy
import numpy as np
data = np.array(data, dtype=float)

# Extrae las columnas de datos
x = data[:, 0]
y1 = data[:, 1] 
y2 = data[:, 2]
y3 = data[:, 3]
y4 = data[:, 4]
y5 = data[:, 5]
y6 = data[:, 6]
y7 = data[:, 7]
y8 = data[:, 8]

# Escala los valores del eje x a picosegundos
x *= 1e12

# Grafica las curvas y agrega etiquetas para la leyenda
plt.plot(x, y2, label='a')
plt.plot(x, y3, label='b')
plt.plot(x, y4, label='c')
plt.plot(x, y5, label='d')
plt.plot(x, y6, label='e')
plt.plot(x, y7, label='f')

# Etiquetas de los ejes y título
plt.xlabel('$Tiempo$ (ps)')
plt.ylabel('Voltaje (V)')  # Cambia la etiqueta del eje y
plt.title('FO4')

# Añade la leyenda
#plt.legend()

# Añade la leyenda
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), ncol=1)


# Muestra la cuadrícula
plt.grid(True)

# Elimina el recuadro de la gráfica
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['bottom'].set_visible(True)
plt.gca().spines['left'].set_visible(True)

# Muestra la gráfica
plt.show()
