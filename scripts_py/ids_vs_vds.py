import matplotlib.pyplot as plt
import csv

# Lista para almacenar los datos
data = []

# Ruta relativa al archivo CSV
csv_file = 'datos_sim/nmod_I_Vds.csv'

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
y1 = -1 * data[:, 1]  # Multiplica la corriente por -1
y2 = -1 * data[:, 2]
y3 = -1 * data[:, 3]
y4 = -1 * data[:, 4]
y5 = -1 * data[:, 5]
y6 = -1 * data[:, 6]
y7 = -1 * data[:, 7]

# Escala los valores del eje y a microamperios
y1 *= 1e6
y2 *= 1e6
y3 *= 1e6
y4 *= 1e6
y5 *= 1e6
y6 *= 1e6
y7 *= 1e6

# Grafica las curvas
plt.plot(x, y1)

plt.plot(x, y2)

plt.plot(x, y3)
plt.text(x[-1], y3[-1], '  $V_{gs}$ = 0.6 V', fontsize=8, ha='left', va='center')
plt.plot(x, y4)
plt.text(x[-1], y4[-1], '  $V_{gs}$ = 0.9 V', fontsize=8, ha='left', va='center')
plt.plot(x, y5)
plt.text(x[-1], y5[-1], '  $V_{gs}$ = 1.2 V', fontsize=8, ha='left', va='center')
plt.plot(x, y6)
plt.text(x[-1], y6[-1], '  $V_{gs}$ = 1.5 V', fontsize=8, ha='left', va='center')
plt.plot(x, y7)
plt.text(x[-1], y7[-1], '  $V_{gs}$ = 1.8 V', fontsize=8, ha='left', va='center')

# Etiquetas de los ejes y título
plt.xlabel('$V_{ds}$ (V)')
plt.ylabel('Corriente (µA)')  # Cambia la etiqueta del eje y
plt.title('Curvas características del NMOS de tamaño mínimo')

# Establece los marcadores del eje x cada 0.2V
plt.xticks(np.arange(min(x), max(x)+0.2, 0.2))


# Muestra la cuadrícula
plt.grid(True)

# Elimina el recuadro de la gráfica
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['bottom'].set_visible(True)
plt.gca().spines['left'].set_visible(True)

# Muestra la gráfica
plt.show()
