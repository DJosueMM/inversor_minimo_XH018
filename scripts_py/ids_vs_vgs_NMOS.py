import matplotlib.pyplot as plt
import numpy as np

# Datos de la tabla
x_values = [0, 0.3, 0.6, 0.9, 1.2, 1.5, 1.8]
y_values = [4.179E-12 ,2.824E-09 ,1.328E-06 ,2.907E-05 ,8.444E-05 ,1.477E-04 ,2.137E-04 ]

# Escalar valores de y_values a microamperios
y_values_micro = [y * 1e6 for y in y_values]

# Crear la figura y los ejes
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

# Graficar en escala normal
ax1.plot(x_values, y_values_micro, linestyle='-', color='blue', label='Escala normal')

# Añadir un punto para el último valor
ax1.scatter(x_values[-1], y_values_micro[-1], color='black', zorder=2)

# Etiqueta de Isat para el último valor
ax1.text(x_values[-1], y_values_micro[-1], f'Isat= {y_values_micro[-1]:.2f} µA', ha='right', va='bottom')

# Ajustar los límites de los ejes y
ax1.set_ylim(0, max(y_values_micro) * 1.1)

# Mostrar la cuadrícula
ax1.grid(True)

# Configurar el eje y para el plot logarítmico
ax2.plot(x_values, y_values_micro, linestyle='-', color='red', label='Escala logarítmica')

# Añadir un punto para el último valor
ax2.scatter(x_values[-1], y_values_micro[-1], color='black', zorder=2)

# Etiqueta de Isat para el último valor
ax2.text(x_values[-1], y_values_micro[-1], f'Isat= {y_values_micro[-1]:.2f} µA', ha='right', va='bottom')

# Ajustar los límites de los ejes
plt.xlim(0, 2)

# Activar escala logarítmica en el eje y
ax2.set_yscale('log')

# Ajustar los límites de los ejes y
ax2.set_ylim(min(y_values_micro), max(y_values_micro) * 10)

# Mostrar la cuadrícula
ax2.grid(True)

# Añadir leyenda
ax1.legend(loc="upper left")
ax2.legend(loc="upper left")

# Añadir título común a los ejes y
plt.ylabel('Corriente (µA)', fontsize=12)
plt.gca().yaxis.set_label_coords(-0.08,1.13)

# Mostrar el título arriba
plt.suptitle('Función de transferencia para NMOS de tamaño mínimo', fontsize=14)

# Mostrar la gráfica
plt.xlabel('$V_{gs}$ (V)')
plt.show()

