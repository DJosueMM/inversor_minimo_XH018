import matplotlib.pyplot as plt
import csv
import numpy as np

# Lista para almacenar los datos
data = []

# Ruta relativa al archivo CSV
csv_file = 'datos_sim/inv_tf_ratios.csv'

# Lee el archivo CSV y guarda los datos en la lista, ignorando la segunda fila (encabezado)
with open(csv_file, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader)  # Saltar la primera fila (metadata)
    next(reader)  # Saltar la segunda fila (encabezado)
    for row in reader:
        data.append(row)

# Convierte los datos a arrays de numpy
data = np.array(data, dtype=float)

# Extrae las columnas de datos
x = data[:, 0]
y1 = 1 * data[:, 1]  # Multiplica la corriente por -1
y2 = 1 * data[:, 2]
y3 = 1 * data[:, 3]
y4 = 1 * data[:, 4]
y5 = 1 * data[:, 5]
y6 = 1 * data[:, 6]
y7 = 1 * data[:, 7]


# Grafica las curvas y agrega etiquetas para la leyenda
plt.plot(x, y1, label='1.0:1')
plt.plot(x, y2, label='1.5:1')
plt.plot(x, y3, label='2.0:1')
plt.plot(x, y4, label='2.5:1')
plt.plot(x, y5, label='3.0:1')
plt.plot(x, y6, label='3.5:1')
plt.plot(x, y7, label='4.0:1')

# Etiquetas de los ejes y título
plt.xlabel('$V_{in}$ (V)')
plt.ylabel('$V_{out}$ (V)')
plt.title('Función de tranferencia de Inversor para distintos ratios')

# Establece los marcadores del eje x cada 0.2V
plt.xticks(np.arange(min(x), max(x)+0.2, 0.2))


# Establece los marcadores del eje x cada 0.2V
plt.yticks(np.arange(min(x), max(x)+0.2, 0.2))

# Muestra la cuadrícula
plt.grid(True)

# Elimina el recuadro de la gráfica
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['bottom'].set_visible(True)
plt.gca().spines['left'].set_visible(True)

# Añade la leyenda
plt.legend()

# Muestra la gráfica
plt.show()
