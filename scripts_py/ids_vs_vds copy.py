import matplotlib.pyplot as plt
import csv

# Lista para almacenar los datos
data = []

# Ruta relativa al archivo CSV
csv_file = 'datos_sim/corners_trans.csv'

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
y0 =  data[:, 6] 
y1 =  data[:, 26] 
y2 =  data[:, 27]
y3 =  data[:, 28]
y4 =  data[:, 29]
y5 =  data[:, 30]

# Escala los valores del eje x 
x *= 1e12

# Grafica las curvas
plt.plot(x, y0)
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.plot(x, y4)
plt.plot(x, y5)


# Etiquetas de los ejes y título
plt.xlabel('Tiempo (ps)')
plt.ylabel('Voltaje (V)')  # Cambia la etiqueta del eje y
plt.title('Esquinas')


# Muestra la cuadrícula
plt.grid(True)

# Elimina el recuadro de la gráfica
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['bottom'].set_visible(True)
plt.gca().spines['left'].set_visible(True)

# Muestra la gráfica
plt.show()
