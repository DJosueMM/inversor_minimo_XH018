import matplotlib.pyplot as plt
import numpy as np

# Datos de la tabla
x_values = [0, 0.3, 0.6, 0.9, 1.2, 1.5, 1.8]
y_values = [4.179E-12 ,2.824E-09 ,1.328E-06 ,2.907E-05 ,8.444E-05 ,1.477E-04 ,2.137E-04 ]

# Escalar valores de y_values a microamperios
y_values_micro = [y * 1e6 for y in y_values]

# Graficar en escala semilogarítmica
plt.plot(x_values, y_values_micro, linestyle='-', label="")

# Agregar un punto para el último valor
plt.scatter(x_values[-1], y_values_micro[-1], color='black', label='Último valor')

# Etiquetas y título
plt.xlabel('$V_{gs}$ (V)')
plt.ylabel('Corriente')
plt.title('Función de transferencia para NMOS de tamaño mínimo')

# Añadir valor de Y como Isat
plt.text(x_values[-1], y_values_micro[-1], f'Isat= {y_values_micro[-1]:.2f} µA', ha='right', va='bottom')

plt.text(x_values[-3], y_values_micro[-3], f'Vds = 1.8 V', ha='right', va='bottom')

# Ajustar los límites de los ejes
plt.xlim(0, 1.8)
plt.ylim(min(y_values_micro), 10000)

# Desactivar escala logarítmica en el eje y
plt.gca().set_yscale('log')


# Muestra la cuadrícula
plt.grid(True)

# Mostrar gráfico
plt.show()




