import matplotlib.pyplot as plt
import numpy as np

# Datos de la tabla
x_values = [0, -0.3, -0.6, -0.9, -1.2, -1.5, -1.8]
y_values = [6.191E-12, 3.450E-09, 1.158E-06, 2.083E-05, 6.388E-05, 1.192E-04, 1.805E-04]

# Escalar valores de y_values a microamperios
y_values_micro = [y * 1e6 for y in y_values]

# Crear la figura y los ejes
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

# Graficar en escala normal
ax1.plot(x_values, y_values_micro, linestyle='-', color='blue', label='Escala normal')

# Añadir un punto para el último valor
ax1.scatter(x_values[-1], y_values_micro[-1], color='black', zorder=2)

# Etiqueta de Isat para el último valor
ax1.text(x_values[-1], y_values_micro[-1], f'Isat= {y_values_micro[-1]:.2f} µA', ha='left', va='bottom')

# Ajustar los límites de los ejes y
ax1.set_ylim(0, max(y_values_micro) * 1.1)

# Mostrar la cuadrícula
ax1.grid(True)

# Configurar el eje y para el plot logarítmico
ax2.plot(x_values, y_values_micro, linestyle='-', color='red', label='Escala logarítmica')

# Añadir un punto para el último valor
ax2.scatter(x_values[-1], y_values_micro[-1], color='black', zorder=2)

# Etiqueta de Isat para el último valor
ax2.text(x_values[-1], y_values_micro[-1], f'Isat= {y_values_micro[-1]:.2f} µA', ha='left', va='bottom')

# Ajustar los límites de los ejes
plt.xlim(-2,0)

# Activar escala logarítmica en el eje y
ax2.set_yscale('log')

# Ajustar los límites de los ejes y
ax2.set_ylim(min(y_values_micro), max(y_values_micro) * 10)

# Mostrar la cuadrícula
ax2.grid(True)

# Añadir leyenda a la derecha
ax1.legend(loc="upper left", bbox_to_anchor=(0.68, 1))
ax2.legend(loc="upper left", bbox_to_anchor=(0.62, 1))

# Añadir título común a los ejes y
plt.ylabel('Corriente (µA)', fontsize=12)
plt.gca().yaxis.set_label_coords(-0.08,1.13)

# Mostrar el título arriba
plt.suptitle('Función de transferencia para PMOS de tamaño mínimo', fontsize=14)

# Mostrar la gráfica
plt.xlabel('$V_{gs}$ (V)')
plt.show()
